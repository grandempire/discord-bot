import discord
from discord.ext import commands
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot Online: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

@bot.command()
@commands.has_permissions(administrator=True)
async def say(ctx, *, message):
    await ctx.send(message)

bot.run(os.getenv("MTQ3Njg2MTE1NTY3MzkwMzEzNA.Gy9oen.ROmUnCTIojfUUzJ3YN7ntlQkJpfLucuBqCoj84"))
