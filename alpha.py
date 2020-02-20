""" Zawoke, written by Zawaken """
import os
import time
import discord
import config as c
from discord.ext import commands

STARTUP_EXTENSIONS = [
        'cogs.admin',
        'cogs.commands',
        'cogs.help'
        ]

bot = commands.Bot(command_prefix=c.prefix, description=c.description)


@bot.event
async def on_ready():
    """ It does this to show that the bot has been started """
    clear = lambda: os.system('clear')
    clear()
    print('------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Command prefix: ' + '"' + c.prefix + '"')
    print('------------------')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(c.game))


@bot.event
async def on_message(message):
    """ No Swore in my server """
    if message.author == bot.user or message.author.bot == True:
        return
    if 'heck' in message.content or 'frick' in message.content:
        await message.add_reaction('🚫')


if __name__ == '__main__':
    for extension in STARTUP_EXTENSIONS:
        bot.load_extension(extension)

    bot.run(c.token, bot=True, reconnect=True)
