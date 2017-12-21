"""
    @commands.command(pass_context=True)
    async def purge(self, ctx):
        \""" Deletes the messages of the specified user. \"""
        print(ctx.message.author.name + ' ' + ctx.message.author.id + ' ' + ctx.message.content)
        userid = ctx.message.author.id
        mcont = ctx.message.content
        if mcont == con.prefix + 'purge':
            await self.bot.delete_message(ctx.message)
            print('command.purge :: no argument')
        elif mcont == con.prefix + 'purge all' and userid == con.owner_id or userid in str(con.dev_id):
            await self.bot.send_message(ctx.message.channel, 'Clearing messages...')
            asyncio.sleep(2)
            async for msg in self.bot.logs_from(ctx.message.channel):
                await self.bot.delete_message(msg)
        else:
            print('error')
            await self.bot.say('Permission Denied')
"""
"""
    @commands.command(pass_context=True)
    async def clear(self, ctx):
        mcont = ctx.message.content
        mcontr = mcont.replace(con.prefix + 'clear', '')
        #async for mcontr in self.bot.logs_from(ctx.message.channel):
            #await self.bot.delete_message(int(mcontr))
"""
"""    @commands.command()
    async def uptime(self):
        \"""Sends info on how long the bot has been online.\"""
        second = time.time() - start_time
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        day, hour = divmod(hour, 24)
        week, day = divmod(day, 7)
        await self.bot.say(week, day, hour, minute, second)
        """