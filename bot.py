# bot.py
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import automation

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='schedule')
async def schedule(ctx):
    await ctx.send('Finding weekly schedule with email ' + os.getenv('FPT_MAIL'))
    await automation.get_schedule()
    await ctx.send(file=discord.File('schedule.png'))

bot.run(TOKEN)
