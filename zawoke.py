#import os
""" . """
import random
#import aiohttp
import requests
#import secrets
#import json
import config as con
import discord
from discord.ext import commands
#from lxml import html


bot = commands.Bot(command_prefix=con.prefix, description=con.description)
BITCOIN_PRICE_URL = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
DATA = requests.get(BITCOIN_PRICE_URL).json()
PRICE_IN_USD = DATA['bpi']['USD']['rate']

@bot.event
async def on_ready():
    """ canker """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name=con.game))


@bot.command(pass_context=True)
async def hello():
    """stuff"""
    await bot.say('Hello')

@bot.command(pass_context=True)
async def flip():
    """stuff"""
    coinflip = random.choice(['heads', 'tails'])
    if coinflip == 'heads':
        await bot.say('```' + coinflip + '```' +
                      'https://www.marshu.com/articles/images-website/articles/presidents-on-' +
                      'coins/quarter-coin-head.jpg')
    else:
        await bot.say('```' + coinflip + '```' + '')

@bot.command(pass_context=True)
async def btc():
    """A command to get BTC price in USD"""
    await bot.say('```' + 'BTC price is currently at $' + PRICE_IN_USD + ' USD' + '```')
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
    elif con.prefix + 'info <@' in mcontent:
        await bot.say('Name = ' + mcontent.replace(con.prefix + 'info', ''))
    else:
        await bot.say('How the hell do you expect me to find info if the info isn\'t readable?')

@bot.command(pass_context=True)
async def hug(ctx):
    """stuff"""
    mcontent = ctx.message.content
    if mcontent == con.prefix + 'hug':
        await bot.say('*If ' + ctx.message.author.name +
                      ' hugs a tree in a forest and no one' +
                      'is around to see it, did it even happen?*')
    elif mcontent == con.prefix + 'hug <@319005959022313483>':
        await bot.say('Ram hugged ' + ctx.message.author.mention + ' back :heart:')
    else:
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
        await bot.say(ctx.message.author.name + ' poked you, ' +
                      mcontent.replace(con.prefix + 'poke', ''))

@bot.command()
async def fuck(context, arg):
    """stuff"""
    await context.send(arg)

@bot.command(pass_context=True)
async def addbtc(ctx):
    """ I want to fix this hahah u thought i was gon say die lol """
    await ctx.create_custom_emoji(server='', name='btc', image='btc.png')
    await bot.say('I am finnish! Perkele')

bot.run(con.token)
