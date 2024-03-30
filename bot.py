import discord
from discord.ext import commands
import os
import random
from options import TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Мой бот-эколог {bot.user} запущен!')

@bot.command()
async def podelki(ctx):
    random_mem = random.choice(os.listdir('images'))
    with open(f'images/{random_mem}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def decom(ctx):
    await ctx.send(f'Мусор разлогается от нескольких дней до 1000 лет!')
    await ctx.send(f'Хочешь узнать что можно сделать из пластиковой бутылки? Если да то - !podelki')
bot.run(TOKEN)  
