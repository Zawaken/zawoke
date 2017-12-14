"""Memes"""
import discord
from discord.ext import commands
import config as con

class Memes():
    """Memes"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def meme(self, ctx, meem: str):
        """ type meme + a meme of your choice
        meme help for help
        """
        if meem == 'sipp':
            await self.bot.send_file(ctx.message.channel, 'img/sipp.png')
        elif meem == 'sight':
            await self.bot.send_file(ctx.message.channel, 'img/lineofsight.png')
        elif meem == 'dipp':
            await self.bot.send_file(ctx.message.channel, 'img/dipp.jpg')
        elif meem == 'memesee':
            await self.bot.send_file(ctx.message.channel, 'img/memesee.jpg')
        elif meem == 'rubik':
            await self.bot.send_file(ctx.message.channel, 'img/rubiks.jpg')
        elif meem == 'saw':
            await self.bot.send_file(ctx.message.channel, 'img/see.png')
        elif meem == 'blonkz':
            await self.bot.send_file(ctx.message.channel, 'img/blonkzeet.png')
        elif meem == 'cucc':
            await self.bot.send_file(ctx.message.channel, 'img/cucc.png')
        elif meem == 'tomto':
            await self.bot.send_file(ctx.message.channel, 'img/tomto.jpg')
        elif meem == 'amgry':
            await self.bot.send_file(ctx.message.channel, 'img/amgry.jpg')
        elif meem == 'blechh':
            await self.bot.send_file(ctx.message.channel, 'img/cupfobleach.jpg')
        elif meem == 'succ':
            await self.bot.send_file(ctx.message.channel, 'img/succ.png')
        else:
            await self.bot.say('```' + meem + ' is not a meme \ntry these:\n    ' +
                               'sipp\n    sight\n    dipp\n    memesee\n    rubik\n    ' +
                               'saw\n    blonkz\n    cuck\n    tomto\n    amgry\n    blechh' +
                               '```')


def setup(bot):
    """makes the memes cog work"""
    bot.add_cog(Memes(bot))
