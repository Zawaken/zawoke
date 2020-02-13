""" Zawoke, written by Zawaken """
import os
import time
import discord
import config as con

bot = discord.Client()


@bot.event
async def on_ready():
    """ It does this to show that the bot has been started """
    clear = lambda: os.system('clear')
    clear()
    print('------------------')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('Command prefix: ' + '"' + con.prefix + '"')
    print('------------------')


bot.run(con.token)
