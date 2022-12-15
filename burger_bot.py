import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random


load_dotenv()
TOKEN = os.environ.get('TOKEN')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} ready')
    print('---------')


@bot.command(description='Test Command')
async def ping(ctx):
    await ctx.send("pong")
    
@bot.command()
async def coinFlip(ctx):
    flip = random.randint(0, 1)
    result = "Heads" if flip == 0 else "Tails"
    await ctx.send(result)

bot.run(TOKEN)