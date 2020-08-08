import os

import discord, requests
from dotenv import load_dotenv
from nba_api.stats.endpoints import commonplayerinfo
from discord.ext import commands

url = 'https://nba-scaper-api.herokuapp.com/'


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

bot = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return #no more infinte loops jet...haha so funny bro
    if message.content.startswith('.score'):
        team = message.content.replace('.score','')
        req = requests.get(url+'score'+team)
        away_score = req.json()['away_score'] #OPTIMIZE THIS
        home_score = req.json()['home_score']
        await message.channel.send(f'Home:{home_score}\nAway:{away_score}')
    if message.content.startswith('.status'):
        await message.channel.send('Skyhook running....')
    if message.cotent.startswith('.schedule'):
        req = requests.get(url+'schedule')
        games = req.json()['games']
        await message.channel.send(games)

     




@bot.command
async def test(ctx, arg):
    await ctx.send(arg)


client.run(TOKEN)