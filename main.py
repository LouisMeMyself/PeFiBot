import asyncio

from discord.ext import commands
from pefiBot.PefiBot import PefiBot

bot = commands.Bot(command_prefix='!')
pefiBot = PefiBot


@bot.event
async def on_ready():
    """starts pefibot"""
    global pefiBot
    pefiBot = PefiBot(bot)
    await pefiBot.on_ready()


@bot.command()
async def pefipic(ctx):
    """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
    await pefiBot.pefipic(ctx)


@bot.command()
async def ipefipic(ctx):
    """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
    await pefiBot.pefipic(ctx)

@bot.command()
async def ratio(ctx):
    """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
    await pefiBot.ratio(ctx)


@bot.command()
async def xpefipic(ctx):
    """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
    await pefiBot.pefipic(ctx)


@bot.command()
async def pefiprice(ctx):
    """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
    await pefiBot.pefiprice(ctx)


@bot.event
async def on_command_error(ctx, error):
    await pefiBot.on_command_error(ctx, error)


if __name__ == '__main__':
    with open(".key", "r") as f:
        key = f.read().replace("\n", "")
    while 1:
        try:
            bot.run(key)
        except:
            print("Error trying to run the pefibot, retrying in 60 seconds")
        asyncio.sleep(60)
