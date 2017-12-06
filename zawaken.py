import os
import discord
import aiohttp
from discord.ext import commands
from data import token
from lxml import html

bot = commands.Bot(command_prefix='>>', description='xd')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)

@bot.command()
async def hello():
    await bot.say('Hello')

bot.run(token)