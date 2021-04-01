import discord
from discord.ext import commands
import asyncio
bot = commands.Bot


while True:
    role = await discord.utils.get(ctx.guild.roles, id=('825411511047684126'))
    await role.edit(colour=discord.Colour.random())
    await asyncio.sleep(10)
























