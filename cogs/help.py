import datetime
import os
import config as c

import discord
from discord.ext import commands

class HelpCog(commands.Cog, name='Help'):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help(self, ctx):
        await ctx.send('This help menu is here to help')


def setup(bot):
    bot.add_cog(HelpCog(bot))
