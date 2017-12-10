# import os
""" . """
import random
# import aiohttp
import requests
# import secrets
# import json
import config as con
import time
import discord
from discord.ext import commands
# from lxml import html


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
async def ping():
    """stuff"""
    await bot.say('Pong')


@bot.command(pass_context=True)
async def test(ctx):
    """ tester """
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    await bot.say(ctx.message.mention.name)


@bot.command(pass_context=True)
async def flip(ctx):
    """ ⚪ = heads, ⚫ = tails """
    coinflip = random.choice(['heads', 'tails'])
    if coinflip == 'heads':
        await bot.add_reaction(ctx.message, '⚪')
    else:
        await bot.add_reaction(ctx.message, '⚫')


@bot.command(pass_context=True)
async def btc():
    """A command to get BTC price in USD"""
    await bot.say('```' + 'BTC price is currently at $' + PRICE_IN_USD + ' USD' + '```')
    # await bot.send_file(ctx.message.channel, 'btc.png')
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
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    mcontent = ctx.message.content
    if mcontent == con.prefix + 'info':
        await bot.say('Name: ' + ctx.message.author.name + '\n'
                      'Id: ' + ctx.message.author.id)
    elif con.prefix + 'info <@' in mcontent:
        await bot.say('Name: ' + mcontent.replace(con.prefix + 'info', '') + '\n' +
                      'Id: ' + mcontent.replace(con.prefix + 'info <@', '').replace('>', ''))
        await bot.delete_message(ctx.message)
    else:
        await bot.say('How the hell do you expect me to find info if the info isn\'t readable?')


@bot.command(pass_context=True)
async def hug(ctx):
    """stuff"""
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    mcontent = ctx.message.content
    if mcontent == con.prefix + 'hug':
        await bot.say('*If ' + ctx.message.author.name +
                      ' hugs a tree in a forest and no one' +
                      'is around to see it, did it even happen?*')
    elif mcontent == con.prefix + 'hug <@' + bot.user.id + '>':
        await bot.say('Ram hugged ' + ctx.message.author.mention + ' back :heart:')
    else:
        await bot.say(ctx.message.author.mention + ' hugged ' +
                      mcontent.replace(con.prefix + 'hug', '') + ' :heart:')
        await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def kys(ctx):
    """ Kill yourself """
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    mcontent = ctx.message.content
    if mcontent == con.prefix + 'kys':
        print('command.kys :: no argument')
        await bot.say('kys, input an argument next time you stoobid')
    else:
        await bot.say('Hey' + mcontent.replace(con.prefix +'kys', '') + ', ' +
                      ctx.message.author.name +
                      ' wants you to die a wonderful death inflicted by yourself!')
        await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def kms(ctx):
    """stuff"""
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    await bot.say('kys ' + ctx.message.author.mention +
                  '\nsuicide hotline = https://www.wikihow.com/Tie-a-Noose')
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def mprint(ctx):
    """stuff"""
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    mcontent = ctx.message.content
    await bot.say(mcontent.replace(con.prefix + 'mprint', ''))


@bot.command(pass_context=True)
async def poke(ctx):
    """Poke"""
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    mcontent = ctx.message.content
    if mcontent == con.prefix + 'poke':
        await bot.say('OwO wat dis, is it a poking? I am not feel it')
    else:
        await bot.say(ctx.message.author.name + ' poked you, ' +
                      mcontent.replace(con.prefix + 'poke', ''))
        await bot.delete_message(ctx.message)

"""
@bot.command()
async def fuck(context, arg):
    \"""stuff\"""
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    await context.send(arg)
"""

@bot.command(pass_context=True)
async def addbtc(ctx, create_custom_emoji, server : discord.Server = None):
    """ I want to fix this hahah u thought i was gon say die lol """
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    await create_custom_emoji(ctx.message.Server, name='btc', image='btc.png')
    await bot.say('I am finnish! Perkele')


@bot.command(pass_context=True)
async def eagames(ctx):
    """ Buy our new expansion pack for 200$ to get darth vader """
    print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
    await bot.say('```Electronic Arts is a ... \n\nTo see the rest of this message paypal' +
                  'me $20k \n Zawaken@waifu.club```')


@bot.command(pass_context=True)
async def purge(ctx):
    """ Deletes the messages of the specified user. """
    print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
    mcont = ctx.message.content
    if mcont == str(con.prefix + 'purge'):
        await bot.delete_message(ctx.message)
        print('command.purge :: no argument')
    elif mcont == con.prefix + 'purge all':
        await bot.send_message(ctx.message.channel, 'Clearing messages...')
        time.sleep(2)
        async for msg in bot.logs_from(ctx.message.channel):
            await bot.delete_message(msg)
    else:
        print('error')


bot.run(con.token)
