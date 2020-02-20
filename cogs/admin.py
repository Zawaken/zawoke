import asyncio
import config as c

import discord
from discord.ext import commands


class AdminCog(commands.Cog, name="admin"):
    """ Commands """

    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(AdminCog(bot))
