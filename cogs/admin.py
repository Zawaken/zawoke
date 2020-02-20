import asyncio
import config as c

import discord
from discord.ext import commands


class AdminCog(commands.Cog, name="admin"):
    """ Commands """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stop', hidden=True)
    async def _stop(self, ctx):
        """ bot == stop """
        await ctx.send('lol')

    @commands.command(name='load', hidden=True)
    async def _load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension('cogs.' + cog)
        except():
            await ctx.message.add_reaction('👎')
        else:
            await ctx.message.add_reaction('👌')


def setup(bot):
    bot.add_cog(AdminCog(bot))
