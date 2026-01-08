import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='Discord.log', encoding='utf8', mode='w')
intents = discord.intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

role_1 = "Honchoss"
@bot.event
async def on_ready():
    print(f'We are ready and online sir {bot.user.name}')

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if "sleep" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} dont use that word!")
    await bot.process_commands(message)

@bot.command()
async def Hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=role_1)
    if role is not None:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} has been given the {role_1}")
    else:
        await ctx.send("Role Doesnt Exist")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=role_1)
    if role is not None:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has his role as {role_1} removed")
    else:
        await ctx.send("Role Doesnt Exist")

@bot.command()
@commands.has_role(role_1)
async def secret(ctx):
    await ctx.send(f"Welcome to the club {ctx.author.mention}")
    
@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"You can't do that")

bot.run(token, log_handler = handler, log_level = logging)