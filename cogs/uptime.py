import asyncio
import discord
import time
from discord.ext import commands
from cogs import utils


class Uptime:
    def __init__(self, bot):
        self.bot = bot
        self.startTime = int(time.time())

    @commands.command(pass_context=True)
    async def uptime(self):
        """lists the uptime of the bot"""
        current_time = int(time.time())
        uptime = utils.ReadableTime(self.startTime, current_time)
        await self.bot.say('I\'ve been up for *{}*.'.format(uptime))

def setup(bot):
    bot.add_cog(Uptime(bot))