import sys
import random
sys.path.insert(0, 'discord.py-self')
import discord
from discord.ext import commands
import json
import asyncio
import tracemalloc
import json

with open('config/config.json', encoding='utf-8') as f:
    config = json.load(f)
credentials = config.get('credentials')
msg_send = config.get('msg_send')
token = config.get('token')
print(credentials)

def randomkeys():
    keys = ["ewazina", "缺点","ჩემი გულწრფელი რეაქცია","condohub","JewelWorld","sex"," 雙人組","kanoyuisdaddy","Deprecation"]
    return random.choice(keys)

def randomlinks():
    links = ["https://link-hub.net/57085/roblox-condo-games","https://link-target.net/57085/roblox-condo-games1","https://link-hub.net/57085/condoes-games"]
    return random.choice(links)


tracemalloc.start()

counter = 1

channel_ids = [
    1109296018979299383,
    1124075731723501619,
    1123255180675268680,
    1115264664465592331,
    1132139311484112976,
    1120728728276848650,
    1069340901375229983,
    1131947638334443570,
    882976290716647424,
    882976433612419092,
    971932523187810304,
    1114978811109441627,
    1131284762292650017
]

#channel_ids = [1059860195204927619,1056829676041011270]
prefix = "!"
bot = commands.Bot(command_prefix=prefix, self_bot=True)
looping = True 

@bot.event
async def on_ready():
    print("=============================================")
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("============================================= \n")
    channels = [bot.get_channel(channel_id) for channel_id in channel_ids]

    # Filter out None values (channels that the bot couldn't find or access)
    channels = [channel for channel in channels if channel]

    if not channels:
        print("Error: Bot could not find/access any of the specified channels.")
        return

    counter = 1
    while looping:
        for channel in channels:
            try:
                await channel.trigger_typing()
                await asyncio.sleep(3)
                random_key = randomkeys()
                random_link = randomlinks()
                message_content = msg_send.replace("{random_key}", random_key).replace("{random_links}", random_link)
                message = await channel.send(message_content)
                print(f"Server: {channel.guild.name} ({channel.guild.id}) | Channel: {channel.name} ({channel.id})")
            except discord.errors.Forbidden:
                print(f"Error: The bot does not have permission to send messages in {channel.guild.name} | {channel.name} ({channel.id})")
            except Exception as e:
                print(f"Error occurred while sending message in {channel.guild.name} | {channel.name} ({channel.id}): {e}")
        counter += 1
        print("Cooldown for an 1 hours!...")
        await asyncio.sleep(1800)
        print("Cooldown for an 30 minutes!...")
        await asyncio.sleep(1200)
        print("Cooldown for an 20 minutes!...")
        await asyncio.sleep(600)
        print("Cooldown ends!")
        await asyncio.sleep(2)
        print("Looping!")


bot.run(token)
