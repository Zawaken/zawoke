import asyncio
import config as c

import discord
from discord.ext import commands


class OwnerCog(commands.Cog, name="Owner"):
    """ OwnerCog """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='stop', hidden=True)
    @commands.is_owner()
    async def _stop(self, ctx):
        """ bot == stop """
        await ctx.send('*Goodbye.*')
        await self.bot.logout()

    @commands.command(name='load', hidden=True)
    @commands.is_owner()
    async def _load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension('cogs.' + cog)
        except(AttributeError, ImportError) as error:
            await ctx.message.add_reaction('👎')
            await ctx.send(f'```py\nCould not load extension {cog}: {error}\n```')
        else:
            await ctx.message.add_reaction('👌')

    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def _unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension('cogs.' + cog)
        except(AttributeError, ImportError) as error:
            await ctx.message.add_reaction('👎')
            await ctx.send(f'```py\nCould not unload extension {cog}: {error}\n```')
        else:
            await ctx.message.add_reaction('👌')

    @commands.command(name='reload', hidden=True)
    @commands.is_owner()
    async def _reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension('cogs.' + cog)
            self.bot.load_extension('cogs.' + cog)
        except(AttributeError, ImportError) as error:
            await ctx.message.add_reaction('👎')
            await ctx.send(f'```py\nCould not reload extension {cog}: {error}')
        else:
            await ctx.message.add_reaction('👌')


    def setup(bot):
        bot.add_cog(OwnerCog(bot))
