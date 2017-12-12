from discord.ext import commands
import discord
import requests
import random

class Cmds:

	def ___init___(self, bot):
		self.bot = bot
		self._last_result = None
		self.sessions = set()

	@commands.command	
	async def ping(self, ctx, *, module):
		"""stuff"""
		await ctx.send('Pong')