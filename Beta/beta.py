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
import commands as com
from utils import context
# from lxml import html


bot = commands.Bot(command_prefix=con.prefix, description=con.description)


async def on_ready():
    """ canker """
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    await bot.change_presence(game=discord.Game(name=con.game))

initial_extensions = (
    'commands.commands'
)

async def process_commands(self, message):
    ctx = await self.get_context(message, cls=context.Context)

    if ctx.command is None:
        return

    async with ctx.aquire():
        await self.invoke(ctx)

async def on_message(self, message):
    if message.author.bot:
        return
    await self.process_commands(message)

bot.run(con.token)
