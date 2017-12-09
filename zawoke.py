import random
#import os
#import aiohttp
import discord
import requests
#import secrets
#import json
import config as con
from discord.ext import commands
#from lxml import html


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
    coinflip = random.choice(['heads', 'tails'])
    if coinflip == 'heads':
        await bot.say('```' + coinflip + '```' +
                      'https://www.marshu.com/articles/images-website/articles/presidents-on-' +
                      'coins/quarter-coin-head.jpg')
    else:
        await bot.say('```' + coinflip + '```' + '')

@bot.command(pass_context=True)
async def btc(ctx):
    """A command to get BTC price in USD"""
    await bot.say('```' + 'BTC price is currently at $' + price_in_usd + ' USD' + '```')
    #await bot.send_file(ctx.message.channel, 'btc.png')
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
    """stuff"""
    mcontent = ctx.message.content
    if mcontent == con.prefix + 'info':
        await bot.say('Name = ' + ctx.message.author.mention)
    else:
        await bot.say('Name = ' + mcontent.replace(con.prefix + 'info', ''))

@bot.command(pass_context=True)
async def hug(ctx):
    """stuff"""
    mcontent = ctx.message.content
    await bot.say(ctx.message.author.mention + ' hugged ' +
                  mcontent.replace(con.prefix + 'hug', '') + ' :heart:')

@bot.command(pass_context=True)
async def kms(ctx):
    """stuff"""
    await bot.say('kys ' + ctx.message.author.mention)

@bot.command(pass_context=True)
async def mprint(ctx):
    """stuff"""
    mcontent = ctx.message.content
    await bot.say(mcontent.replace(con.prefix + 'mprint', ''))

@bot.command(pass_context=True)
async def poke(ctx):
    """Poke"""
    mcontent = ctx.message.content
    if mcontent == con.prefix + 'poke':
        await bot.say('OwO wat dis, is it a poking? I am not feel it')
    else:
        await bot.say(ctx.message.author.name + ' poked you, ' + mcontent.replace(con.prefix + 'poke', ''))

@bot.command()
async def fuck(context, arg):
    """stuff"""
    await context.send(arg)

@bot.command(pass_context=True)
async def addbtc(ctx, create_custom_emoji):
    await ctx.create_custom_emoji(server='85475567696117760', name='btc', image='btc.png')
    await bot.say('I am finnish! Perkele')

bot.run(con.token)