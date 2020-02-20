""" Zawoke, written by Zawaken """
import os
import time
import discord
import config as c
from discord.ext import commands

STARTUP_EXTENSIONS = [
        'cogs.admin',
        'cogs.commands'
        ]

bot = commands.Bot(command_prefix=c.prefix, description=c.description)


@bot.event
async def on_ready():
    """ It does this to show that the bot has been started """
    clear = lambda: os.system('clear')
    clear()
    print('-' * len(str(bot.user.id)))
    print('Logged in as:')
    print(f'{bot.user.name} - {bot.user.id}')
    print(f'Command prefix: "{c.prefix}"')
    print(f'{bot.user.name} is currently running on {len(bot.servers)} servers')
    print('-' * len(str(bot.user.id)))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(c.game))


@bot.event
async def on_message(message):
    """ No Swore in my server """
    if message.author == bot.user or message.author.bot == True:
        return
    if 'heck' in message.content or 'frick' in message.content:
        await message.add_reaction('🚫')

    await bot.process_commands(message)


if __name__ == '__main__':
    for extension in STARTUP_EXTENSIONS:
        bot.load_extension(extension)

    bot.run(c.token, bot=True, reconnect=True)
