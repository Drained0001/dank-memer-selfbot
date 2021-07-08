import discord
import asyncio
from discord.ext import commands
import random

class auto_hunt(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.daguildid = 828560582495305769
        self.dank_memer_id = 270904126974590976

    @commands.command(name="To start the auto hunt, type *pls hunt* and itll begin.")
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
        if "pls hunt" in message.content.lower():
            the_time = random.randint(5, 10)
            print(f'Sending hunt in {the_time} seconds')
            await asyncio.sleep(the_time)
            await ctx.send('pls hunt')

        elif f"<@{self.client.user.id}>" in message.content and "god forbid you find something innocent like a duck" in message.content:
            if "`h\ufeffo\ufeffl\ufeffy\ufeff \ufeffs\ufeffh\ufeffi\ufefft\ufeff \ufeffa\ufeff \ufeffd\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff" in message.content:
                await ctx.send('holy shit a dragon')
            elif "`i\ufeffm\ufeffm\ufeffa\ufeff \ufeffk\ufeffi\ufeffl\ufeffl\ufeff \ufefft\ufeffh\ufeffi\ufeffs\ufeff \ufeffd\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff`" in message.content:
                await ctx.send('imma kill this dragon')
            elif "o\ufeffh\ufeff \ufeffl\ufeffo\ufeffo\ufeffk\ufeff \ufeffa\ufeff \ufeffd\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff" in message.content:
                await ctx.send("oh look a dragon")

            elif "o\ufeffh\ufeff \ufefff\ufeffr\ufeffi\ufeffc\ufeffk\ufeff \ufeffa\ufeff \ufeffd\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff" in message.content:
                await ctx.send("oh frick a dragon")

            elif "I\ufeff \ufefff\ufeffo\ufeffr\ufeffg\ufeffo\ufefft\ufeff \ufeffd\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff \ufeffr\ufeffe\ufeffp\ufeffe\ufeffl\ufeffl\ufeffe\ufeffn\ufefft\ufeff \ufeffa\ufeffg\ufeffa\ufeffi\ufeffn\ufeff" in message.content:
                await ctx.send("i forgot the dragon repellent again")

            elif "w\ufeffh\ufeffy\ufeff \ufeffd\ufeffi\ufeffd\ufeffn\ufeff'\ufefft\ufeff \ufeffI\ufeff \ufeffj\ufeffu\ufeffs\ufefft\ufeff \ufeffg\ufeffo\ufeff \ufefff\ufeffi\ufeffs\ufeffh\ufeffi\ufeffn\ufeffg\ufeff" in message.content:
                await ctx.send("why didnt i just go fishing")

            elif "p\ufeffl\ufeffs\ufeff \ufeffn\ufeffo\ufeff \ufeffe\ufeffa\ufefft\ufeffi\ufeffn\ufeffg\ufeff \ufeffm\ufeffe\ufeff" in message.content:
                await ctx.send("pls no eating me")

            elif "o\ufeffh\ufeff \ufeffl\ufeffo\ufeffo\ufeffk\ufeff \ufeffa\ufeff \ufeffd\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff" in message.content:
                await ctx.send("oh look a dragon")

            elif "w\ufeffo\ufeffa\ufeffh\ufeff \ufefft\ufeffh\ufeffo\ufeffs\ufeffe\ufeff \ufeffa\ufeffr\ufeffe\ufeff \ufeffs\ufeffo\ufeffm\ufeffe\ufeff \ufefft\ufeffo\ufeffo\ufefft\ufeffh\ufeffe\ufeffr\ufeffs\ufeff" in message.content:
                await ctx.send("woah those are some toothers")

            elif "d\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff \ufeffs\ufeffa\ufeffy\ufeffs\ufeff \ufeffr\ufeffa\ufeffw\ufeffr\ufeff" in message.content:
                await ctx.send("dragon says rawr")

            elif "e\ufeffa\ufefft\ufeff \ufeffl\ufeffe\ufeffa\ufeffd\ufeff \ufeffd\ufeffr\ufeffa\ufeffg\ufeffo\ufeffn\ufeff" in message.content:
                await ctx.send("eat lead dragon")
            
            else:
                await ctx.send('Couldnt auto answer.')
                print(message.content.split(" "))

        else:
            return
        
def setup(client):
    client.add_cog(auto_hunt(client))
