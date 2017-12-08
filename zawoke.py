import random
import os
import aiohttp
import discord
import requests
#import secrets
import json
import config as con
from discord.ext import commands
from lxml import html


bot = commands.Bot(command_prefix=con.prefix, description=con.description)
bitcoin_price_url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
data = requests.get(bitcoin_price_url).json()
price_in_usd = data['bpi']['USD']['rate']

@bot.event
async def on_ready():
    """ canker """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name=con.game))

@bot.command(pass_context=True)
async def hello(ctx):
    """stuff"""
    await bot.say('Hello')

@bot.command(pass_context=True)
async def flip(ctx):
    """stuff"""
    flip = random.choice(['heads', 'tails'])
    if flip = 'heads':
        await bot.say('```' + flip + '```' + 'https://www.marshu.com/articles/images-website/articles/presidents-on-coins/quarter-coin-head.jpg')
    else:
        await bot.say('```' + flip + '```' + '')

@bot.command(pass_context=True)
async def btc(ctx):
    """A command to get BTC price in USD"""
    await bot.say('BTC price is currently at $' + price_in_usd + ' USD')

"""
@bot.command(pass_context=True)
async def joke(cmd, message, args):
    with open('jokes.json') as jokes_file:
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

@bot.command(pass_context=True)
async def huguser(ctx):
    await bot.say(ctx.message.author.mention + ' hugged ' + ctx.message.content[10:] + ' :heart:')

@bot.command(pass_context=True)
async def kms(ctx):
    await bot.say('kys ' + ctx.message.author.mention)

@bot.command(pass_context=True)
async def print(ctx):
    await bot.say(ctx.message.content[8:])

@bot.command()
async def ctx(ctx, args):
    await ctx.send(args)

bot.run(con.token)