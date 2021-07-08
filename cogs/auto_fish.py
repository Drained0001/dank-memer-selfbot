import discord
import asyncio
from discord.ext import commands
import random
from random import randint
import time
import datetime

class auto_fish(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.daguildid = 0
        self.dank_memer_id = 270904126974590976
        self.start_time = None

    @commands.command(name="To start the auto fish, type *pls fish* and itll begin.")
    async def _bruh(self, ctx):
        return

    @commands.Cog.listener()
    async def on_message(self, message):
        answer = message
        ctx = message.channel
        try:
            if message.guild.id != self.daguildid:
                return
        except:
            return
        if message.author.id not in [self.client.user.id, self.dank_memer_id]:
            return
        if "pls fish" in message.content.lower():
            if self.start_time == None:
                self.start_time = datetime.datetime.utcnow()
            else:
                delta_uptime = datetime.datetime.utcnow() - self.start_time
                hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
                minutes, seconds = divmod(remainder, 60)
                days, hours = divmod(hours, 24)
                if hours == 1:
                    print('Stopping Fishing incase of automod detection. Starting again in 15 minutes')
                    await asyncio.sleep(900)
            the_time = random.randint(5, 10)
            await asyncio.sleep(the_time)
            await ctx.send('pls fish')

        elif f"<@{self.client.user.id}> the fish is too strong!" in message.content:
            if "`B\ufeffi\ufeffg\ufeff \ufeffb\ufeffa\ufeffi\ufefft\ufeff \ufeffc\ufeffa\ufefft\ufeffc\ufeffh\ufeffe\ufeffs\ufeff \ufeffb\ufeffi\ufeffg\ufeff \ufefff\ufeffi\ufeffs\ufeffh\ufeff" in message.content:
                await ctx.send('big bait catches big fish')
            elif "h\ufeffo\ufeffo\ufeffk\ufeff \ufeffl\ufeffi\ufeffn\ufeffe\ufeff \ufeffa\ufeffn\ufeffd\ufeff \ufeffs\ufeffi\ufeffn\ufeffk\ufeffe\ufeffr\ufeff" in message.content:
                await ctx.send('hook line and sinker')
            elif "g\ufeffe\ufefft\ufeff \ufefft\ufeffh\ufeffe\ufeff \ufeffc\ufeffa\ufeffm\ufeffe\ufeffr\ufeffa\ufeff \ufeffr\ufeffe\ufeffa\ufeffd\ufeffy\ufeff \ufeffm\ufeffo\ufeffm\ufeff" in message.content:
                await ctx.send('get the camera ready mom')
            elif "w\ufeffo\ufeffa\ufeffh\ufeff \ufeffa\ufeff \ufeffb\ufeffi\ufeffg\ufeff \ufeffo\ufeffn\ufeffe\ufeff" in message.content:
                await ctx.send('woah a big one')
            elif "g\ufeffl\ufeffu\ufeffb\ufeff \ufeffg\ufeffl\ufeffu\ufeffb\ufeff \ufeffg\ufeffl\ufeffu\ufeffb\ufeff" in message.content:
                await ctx.send('glub glub glub')
            elif "f\ufeffi\ufeffs\ufeffh\ufeff \ufefff\ufeffi\ufeffs\ufeffh\ufeff \ufefff\ufeffi\ufeffs\ufeffh\ufeff \ufefff\ufeffi\ufeffs\ufeffh\ufeffy\ufeff" in message.content:
                await ctx.send('fish fish fish fishy')
            elif "t\ufeffh\ufeffi\ufeffs\ufeff \ufeffi\ufeffs\ufeff \ufeffv\ufeffe\ufeffr\ufeffy\ufeff \ufefff\ufeffi\ufeffs\ufeffh\ufeffy\ufeff" in message.content:
                await ctx.send('this is very fishy')
            elif "b\ufeffi\ufeffg\ufeff \ufeffb\ufeffi\ufeffg\ufeff \ufefff\ufeffi\ufeffs\ufeffh\ufeffy\ufeff" in message.content:
                await ctx.send("big big fishy")
            else:
                print(message.content.split(" "))

        else:
            return
        
def setup(client):
    client.add_cog(auto_fish(client))
