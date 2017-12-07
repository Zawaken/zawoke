import random
import os
import aiohttp
import discord
from discord.ext import commands
from data import token
from lxml import html

bot = commands.Bot(command_prefix='>>', description='xd')

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

bot.run(token)