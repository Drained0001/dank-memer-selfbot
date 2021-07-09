import discord
import asyncio
from discord.ext import commands
import random
import time
import datetime

class auto_dig(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.daguildid = 0
        self.dank_memer_id = 270904126974590976
        self.channel = 0
        self.start_time = None

    @commands.command(name="To start the auto dig, type *pls dig* and itll begin.")
    async def _bruh(self, ctx):
        return

    @commands.Cog.listener()
    async def on_message(self, message):
        answer = message
        ctx = self.client.get_channel(self.channel)
        try:
            if message.guild.id != self.daguildid:
                return
            if message.channel.id != self.channel:
                return
        except:
            return
        if message.author.id not in [self.client.user.id, self.dank_memer_id]:
            return
        if "pls dig" in message.content.lower():
            if self.start_time == None:
                self.start_time = datetime.datetime.utcnow()
            else:
                delta_uptime = datetime.datetime.utcnow() - self.start_time
                hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
                minutes, seconds = divmod(remainder, 60)
                days, hours = divmod(hours, 24)
                if hours == 1:
                    print('Stopping Digging incase of automod detection. Starting again in 15 minutes')
                    await asyncio.sleep(900)
            the_time = random.randint(5, 10)
            await asyncio.sleep(the_time)
            await ctx.send('pls dig')

        else:
            return
        
def setup(client):
    client.add_cog(auto_dig(client))
