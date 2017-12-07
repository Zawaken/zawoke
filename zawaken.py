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

@bot.command(pass_context=True)
async def 

bot.run(token)