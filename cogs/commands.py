""" Commands """
import random
from discord.ext import commands
import discord
import requests
import config as con

BITCOIN_PRICE_URL = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
DATA = requests.get(BITCOIN_PRICE_URL).json()
PRICE_IN_USD = DATA['bpi']['USD']['rate']

class Commands:
    """Commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self):
        """Pings the bot host"""
        await self.bot.say('Pong')

    @commands.command(pass_context=True)
    async def flip(self, ctx):
        """ ⚪ = heads, ⚫ = tails """
        coinflip = random.choice(['heads', 'tails'])
        if coinflip == 'heads':
            await self.bot.add_reaction(ctx.message, '⚪')
        else:
            await self.bot.add_reaction(ctx.message, '⚫')

    @commands.command(pass_context=True)
    async def info(self, ctx):
        """Grabs the info of the person you input"""
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        mcontent = ctx.message.content
        if mcontent == con.prefix + 'info':
            await self.bot.say('Name: ' + ctx.message.author.name + '\n'
                               'Id: ' + ctx.message.author.id)
        elif con.prefix + 'info <@' in mcontent:
            await self.bot.say('Name: ' + mcontent.replace(con.prefix + 'info', '') + '\n' +
                               'Id: ' + mcontent.replace(con.prefix +
                                                         'info <@', '').replace('>', ''))
            await self.bot.delete_message(ctx.message)
        else:
            await self.bot.say('How the hell do you expect me to find info' +
                               'if the info isn\'t readable?')

    @commands.command(pass_context=True)
    async def poke(self, ctx):
        """Poke the bot or a person"""
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        mcontent = ctx.message.content
        if mcontent == con.prefix + 'poke':
            await self.bot.say('OwO wat dis, is it a poking?')
        else:
            await self.bot.say(ctx.message.author.name + ' poked you, ' +
                               mcontent.replace(con.prefix + 'poke', ''))
            await self.bot.delete_message(ctx.message)

    @commands.command()
    async def btc(self):
        """A command to get BTC price in USD"""
        await self.bot.say('```' + 'BTC price is currently at $' + PRICE_IN_USD + ' USD' + '```')

    @commands.command(pass_context=True)
    async def hug(self, ctx):
        """Hug a person of your choice ❤"""
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        mcontent = ctx.message.content
        if mcontent == con.prefix + 'hug':
            await self.bot.say('*If ' + ctx.message.author.name +
                               ' hugs a tree in a forest and no one' +
                               'is around to see it, did it even happen?*')
        elif mcontent == con.prefix + 'hug <@' + self.bot.user.id + '>':
            await self.bot.say('Ram hugged ' + ctx.message.author.mention + ' back :heart:')
        else:
            await self.bot.say(ctx.message.author.mention + ' hugged ' +
                               mcontent.replace(con.prefix + 'hug', '') + ' :heart:')
            await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True)
    async def kys(self, ctx):
        """ Kill yourself """
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        mcontent = ctx.message.content
        if mcontent == con.prefix + 'kys':
            print('command.kys :: no argument')
            await self.bot.say('kys, input an argument next time you stoobid')
        else:
            await self.bot.say('Hey' + mcontent.replace(con.prefix +'kys', '') + ', ' +
                               ctx.message.author.name +
                               ' wants you to die a wonderful death inflicted by yourself!')
            await self.bot.delete_message(ctx.message)

    @commands.command()
    async def say(self, *argumento: str):
        """outputs whatever argument you put after the command"""
        await self.bot.say(argumento)

def setup(bot):
    """makes sure that this file is added as a Cog"""
    bot.add_cog(Commands(bot))
