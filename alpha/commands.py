from discord.ext import commands
import discord
import requests
import random
import time
import config as con

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

    @commands.command(pass_context=True)
    async def purge(self, ctx, bot):
        """ Deletes the messages of the specified user. """
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        mcont = ctx.message.content
        if mcont == con.prefix + 'purge':
            await self.bot.delete_message(ctx.message)
            print('command.purge :: no argument')
        elif mcont == con.prefix + 'purge all':
            await self.bot.send_message(ctx.message.channel, 'Clearing messages...')
            time.sleep(2)
            async for msg in bot.logs_from(ctx.message.channel):
                await self.bot.delete_message(msg)
        else:
            print('error')

def setup(bot):
    bot.add_cog(Cmds(bot))
