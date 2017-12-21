""" Zawoke """
import os
import time
import discord
from discord.ext import commands
import config as con
from cogs import utils

STARTUP_EXTENSIONS = ["cogs.commands", "cogs.admin", "cogs.memes", "cogs.uptime"]

bot = commands.Bot(command_prefix=con.prefix, description=con.description)

@bot.event
async def on_ready():
    """ canker """
    clear = lambda: os.system('cls')
    clear()
    print('------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Command prefix: ' + '\"' + con.prefix + '\"')
    print(' ')
    print('Bot currently running on {} servers:'.format(len(bot.servers)))
    for s in bot.servers:
        print(' - ' + s.name)
    print('------------------')
    await bot.change_presence(game=discord.Game(name=con.game))

@bot.event
async def on_message(message):
    """ NO SWEARING IN MY CRISTIAN SERVER """
    if 'heck' in message.content or 'frick' in message.content:
        await bot.send_file(message.channel, 'img/noswearing.jpg')

    await bot.process_commands(message)

@bot.command()
async def load(extension_name: str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as excom:
        await bot.say("```py\n{}: {}\n```".format(type(excom).__name__, str(excom)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name: str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def reload(extension_name: str):
    """Loads an extension."""
    try:
        bot.unload_extension(extension_name)
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as excom:
        await bot.say("```py\n{}: {}\n```".format(type(excom).__name__, str(excom)))
        return
    await bot.say("{} reloaded.".format(extension_name))

@bot.command()
async def add(left: int, right: int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def repeat(times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)
        print(i)

if __name__ == "__main__":
    for extension in STARTUP_EXTENSIONS:
        try:
            bot.load_extension(extension)
        except Exception as excom:
            exc = '{}: {}'.format(type(excom).__name__, excom)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(con.token)
