import sys
import random
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands
import json
import asyncio
import tracemalloc

with open('config/config.json', encoding='utf-8') as f:
    config = json.load(f)
credentials = config.get('credentials')
msg_send = config.get('msg_send')
token = config.get('token')
print(credentials)

def randomkeys():
    # Removed array; now returns a single default key
    return "default_key"

def randomlinks():
    # Removed array; now returns a single default link
    return "https://default-link.com"

tracemalloc.start()

prefix = "!"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
looping = True 

@bot.event
async def on_ready():
    print("=============================================")
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("============================================= \n")

    # No channel list now; must fetch channels individually or modify logic
    # Example: single channel ID
    channel_id = 1109296018979299383
    channel = bot.get_channel(channel_id)
    if not channel:
        print(f"Error: Bot could not find/access the channel {channel_id}.")
        return

    counter = 1
    while looping:
        try:
            await channel.trigger_typing()
            await asyncio.sleep(3)
            random_key = randomkeys()
            random_link = randomlinks()
            message_content = msg_send.replace("{random_key}", random_key).replace("{random_links}", random_link)
            await channel.send(message_content)
            print(f"Server: {channel.guild.name} ({channel.guild.id}) | Channel: {channel.name} ({channel.id})")
        except discord.errors.Forbidden:
            print(f"Error: The bot does not have permission to send messages in {channel.guild.name} | {channel.name} ({channel.id})")
        except Exception as e:
            print(f"Error occurred while sending message in {channel.guild.name} | {channel.name} ({channel.id}): {e}")
        
        counter += 1
        print("Cooldown for an 1 hour!...")
        await asyncio.sleep(1800)
        print("Cooldown for 30 minutes!...")
        await asyncio.sleep(1200)
        print("Cooldown for 20 minutes!...")
        await asyncio.sleep(600)
        print("Cooldown ends!")
        await asyncio.sleep(2)
        print("Looping!")

bot.run(token)
