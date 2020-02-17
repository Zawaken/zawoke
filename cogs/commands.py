import random
import time
from discord.ext import commands
import discord
import requests
import config as c


class CommandsCog(commands.Cog, name="commands"):
    """ CommandsCog """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def _ping(self, ctx):
        await ctx.send('pong')

def setup(bot):
    bot.add_cog(CommandsCog(bot))
