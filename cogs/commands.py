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

    @commands.command(name='coinflip', aliases=['flip', 'cf'])
    async def _flip(self, ctx):
        coinflip = random.choice(['heads', 'tails'])
        if coinflip == 'heads':
            await ctx.message.add_reaction('⚪')
        elif coinflip == 'tails':
            await ctx.message.add_reaction('⚫')

    @commands.command(name='btcprice', aliases=['btc', 'bitcoin'])
    async def _btcprice(self, ctx):
        BITCOIN_PRICE_URL = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
        DATA = requests.get(BITCOIN_PRICE_URL).json()
        PRICE_IN_USD = DATA['bpi']['USD']['rate']
        await ctx.send(f'```Bitcoin\'s current value is ${PRICE_IN_USD}```')


def setup(bot):
    bot.add_cog(CommandsCog(bot))
