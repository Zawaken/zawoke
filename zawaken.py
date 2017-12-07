import random
import os
import discord
import aiohttp
from discord.ext import commands
from data import token
from lxml import html

bot = commands.Bot(command_prefix='>>', description='xd')

@bot.event
async def on_ready():
    """ canker """
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def hello():
    await bot.say('Hello')

@bot.command()
async def flip():
    flip = random.choice(['heads', 'tails'])
    await bot.say(flip)

bot.run(token)