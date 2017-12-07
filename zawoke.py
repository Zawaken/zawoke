import random
import os
import aiohttp
import discord
from discord.ext import commands
from data import token
from lxml import html
import requests
import secrets
import json


bot = commands.Bot(command_prefix='>>', description='xd')
bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
data = requests.get(bitcoin_price_url).json()
price_in_usd = data['bpi']['USD']['rate']

@bot.event
async def on_ready():
    """ canker """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name='with herself'))

@bot.command(pass_context=True)
async def hello(ctx):
    """stuff"""
    await bot.say('Hello')

@bot.command(pass_context=True)
async def flip(ctx):
    """stuff"""
    flip = random.choice(['heads', 'tails'])
    await bot.say(flip)

@bot.command(pass_context=True)
async def btc(ctx):
    """A command to get BTC price in USD"""
    await bot.say('BTC price is currently at $' + price_in_usd + ' USD')

"""
@bot.command(pass_context=True)
async def joke(cmd, message, args):
    with open('dadjokes.json') as jokes_file:
        jokes = jokes_file.read()
        jokes = json.loads(jokes)
    joke_list = jokes['JOKES']
    joke = secrets.choice(joke_list)
    joker = joke['joke']
    embed = discord.Embed(color=0xFFDC5D)
    embed.add_field(name='Have an offensive joke', value=f'{joker}')
    await message.channel.send(None, embed=embed)
"""

@bot.command(pass_context=True)
async def info(ctx):
    await bot.say('Name = ' + ctx.message.author.mention)

@bot.command(pass_context=True)
async def hug(ctx):
    await bot.say('Ram hugged ' + ctx.message.author.mention + ' back :heart:')

bot.run(token)