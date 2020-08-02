""" Zawoke, written by Zawaken """
import os
import time
import discord
import config as c
from discord.ext import commands

STARTUP_EXTENSIONS = [
        'cogs.admin',
        'cogs.commands',
        'cogs.owner'
        ]

def get_prefix(bot, message):
    return commands.when_mentioned_or(*c.prefixes)(bot, message)

bot = commands.Bot(command_prefix=get_prefix, description=c.description)


@bot.event
async def on_ready():
    """ It does this to show that the bot has been started """
    clear = lambda: os.system('clear')
    clear()
    print('-' * len(str(bot.user.id)))
    print('Logged in as:')
    print(f'{bot.user.name} - {bot.user.id}')
    print(f'Command prefixes: "{str(c.prefixes).strip("[]")}"')
    print(f'{bot.user.name} is currently running in {len(bot.guilds)} servers')
    print('-' * len(str(bot.user.id)))
    if c.docker_status:
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(c.docker_game))
    else:
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

    bot.run(c.d['botToken'], bot=True, reconnect=True)
