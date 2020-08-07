import os

import discord, requests
from dotenv import load_dotenv
from nba_api.stats.endpoints import commonplayerinfo


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

pic_ext = ['.jpg','.png','.jpeg']


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == '.ping':
        await message.channel.send('pong')
        await message.channel.send(file=discord.File('lebron.jpg'))





    

client.run(TOKEN)