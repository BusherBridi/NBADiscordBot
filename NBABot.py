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
        await message.channel.send('Skyhook running!')
    if message.content.startswith('.embed'):
        embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embed.add_field(name="Field1", value="hi", inline=False)
        embed.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embed)

        


@bot.command
async def test(ctx, arg):
    await ctx.send(arg)


client.run(TOKEN)