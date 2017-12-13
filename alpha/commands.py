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

def setup(bot):
    bot.add_cog(Cmds(bot))
