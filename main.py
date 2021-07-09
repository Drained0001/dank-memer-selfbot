import discord
from discord.ext import commands
import random
import os
from colorama import Fore, init
from os import system

client = commands.Bot(command_prefix="dm!", self_bot=True)

for cog in list(client.cogs):
    client.load_extension(f"cogs.{cog}")

@client.command()
async def unload(ctx, extension):
    if ctx.author.id == client.user.id:
        client.unload_extension(f'cogs.{extension}')

@client.command()
async def load(ctx, extension):
    if ctx.author.id == client.user.id:
        client.load_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    if ctx.author.id == client.user.id:
        client.unload_extension(f'cogs.{extension}')
        client.load_extension(f'cogs.{extension}')

@client.command()
async def quit(ctx):
    exit()

@client.command()
async def show_inv(ctx, amt:int):
    await ctx.message.delete()
    for a in range(amt):
        msg = await ctx.send(f"pls inv {a+1}")
        await msg.delete()

client.run("discord account token", bot=False)
