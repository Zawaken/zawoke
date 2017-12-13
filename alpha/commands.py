from discord.ext import commands
import discord
import requests
import random

class Cmds:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self):
        """stuff"""
        await self.bot.say('Pong')
    
    @commands.command(pass_context=True)
    async def flip(self, ctx):
        coinflip = random.choice(['heads', 'tails'])
        if coinflip == 'heads':
            await self.bot.add_reaction(ctx.message, '⚪')
        else:
            await self.bot.add_reaction(ctx.message, '⚫')

def setup(bot):
    bot.add_cog(Cmds(bot))
