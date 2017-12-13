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
    async def test(self, bot, ctx):
        """ tester """
        print(ctx.message.author.name + ctx.message.author.id + ctx.message.content)
        await bot.say(ctx.message.mention.name)

def setup(bot):
    bot.add_cog(Cmds(bot))
