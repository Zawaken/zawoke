""" Admin Commands"""
import asyncio
import config as con
import discord
from discord.ext import commands

class Admin:
    """Commands"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def stop(self, ctx):
        """stops the bot"""
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        userid = ctx.message.author.id
        if userid == con.owner_id or userid in str(con.dev_id):
            await self.bot.say('*Goodbye...*')
            asyncio.sleep(2)
            await self.bot.logout()
        else:
            await self.bot.say('Permission Denied')

    @commands.command(pass_context=True)
    async def purge(self, ctx, messages: int):
        """ Deletes the messages of the specified user. """
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        mcont = ctx.message.content
        if mcont == con.prefix + 'purge':
            await self.bot.delete_message(ctx.message)
            print('command.purge :: no argument')
        elif mcont == con.prefix + 'purge all':
            await self.bot.send_message(ctx.message.channel, 'Clearing messages...')
            asyncio.sleep(2)
            async for msg in self.bot.logs_from(ctx.message.channel):
                await self.bot.delete_message(msg)
        else:
            print('error')

def setup(bot):
    """Makes it so Cogs actually work"""
    bot.add_cog(Admin(bot))
