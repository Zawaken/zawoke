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
    async def purge(self, ctx, amount: str):
        """Deletes the messages of the specified user (hopefully)"""
        userid = ctx.message.author.id
        mcontent = ctx.message.content
        if userid == con.owner_id or userid in str(con.dev_id):
            await self.bot.delete_message(ctx.message)
            if amount == str('all'):
                delet = await self.bot.purge_from(ctx.message.channel, limit=500)
                await self.bot.send('Bulk cleared **{}** messages'.format(len(delet)))
                async for msg in self.bot.logs_from(ctx.message.channel):
                    await self.bot.delete_message(msg)
            elif int(amount) > 0:
                counter = 0
                for counter in range(int(amount)):
                    async for msg in self.bot.logs_from(ctx.message.channel):
                        if int(counter) >= int(amount):
                            return
                        else:
                            await self.bot.delete_message(msg)
                        counter += 1
            elif int(amount) > 0 and str('<@') in mcontent:
                print('This is tester to check if it work')

def setup(bot):
    """Makes it so Cogs actually work"""
    bot.add_cog(Admin(bot))
