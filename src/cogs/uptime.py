import asyncio
import time

import discord
from discord.ext import commands
from cogs.utils import uptime

class UptimeCog(commands.Cog, name="uptime"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="uptime")
    async def _uptime(self, ctx):
        current_time = int(time.time)
        up_time = uptime.ReadableTime(self.startTime, current_time)
        await ctx.send(f'I\'ve been up for {up_time}')


def setup(bot):
    bot.add_cog(uptime(bot))
