import os

import discord, requests
from dotenv import load_dotenv
from nba_api.stats.endpoints import commonplayerinfo


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == 'ping':
        await message.channel.send('pong')

client.run(TOKEN)