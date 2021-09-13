import asyncio
import json
import typing
from datetime import datetime

import discord
from discord import NotFound
from discord.ext import commands

from constants import Constants, Channels
from pefiBot import PefiPic, PangoAPI
from pefiBot.PefiContract import getIPefiRatio


class PefiBot:
    pefiPic_ = PefiPic.PefiPic()
    bot = commands.Bot

    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        """starts pefibot"""
        print('pefiBot have logged in as {0.user}'.format(self.bot))
        self.bot.loop.create_task(self.pefiTicker())

    async def ratio(self, ctx):
        """show the current iPEFI:PEFI ratio"""
        if ctx.message.channel.id == Constants.COMMAND_CHANNEL_ID:
            ratio = getIPefiRatio()
            await ctx.reply("Current iPEFI:PEFI ratio: {}".format(round(ratio, 4)))

    async def pefiTicker(self):
        while 1:
            try:
                print("pefiTicker is up")
                while 1:
                    price = await PangoAPI.getPefiPrice()
                    activity = "PEFI: ${}".format(round(price, 2))
                    await self.bot.change_presence(
                        activity=discord.Activity(type=discord.ActivityType.watching, name=activity))
                    await asyncio.sleep(60)
            except ConnectionError:
                print("Connection error, retrying in 60 seconds...")
            except AssertionError:
                print("Assertion Error, retrying in 60 seconds...")
            except KeyboardInterrupt:
                print(KeyboardInterrupt)
                break
            await asyncio.sleep(60)

    async def pefipic(self, ctx):
        """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
        if ctx.message.channel.id == Constants.PEFIPIC_CHANNEL_ID:
            try:
                answer = self.pefiPic_.do_profile_picture(ctx.message.content)
                await ctx.reply(answer[0], file=answer[1])
            except ValueError:
                await ctx.reply(embed=self.errorOnCommand(Constants.PEFI_PICTURE_COMMAND))
        return

    async def pefiprice(self, ctx):
        """command that return the price of the penguin token"""
        if ctx.message.channel.id in Constants.PEFIPRICE_CHANNEL_ID:
            price = await PangoAPI.getPefiPrice()
            e = discord.Embed(title="Penguin Token",
                              url="https://info.pangolin.exchange/#/token/0xe896cdeaac9615145c0ca09c8cd5c25bced6384c",
                              description="Price: ${}".format(round(price, 2)),
                              color=0xF24E4D)
            await ctx.send(embed=e)
        return

    async def on_command_error(self, ctx, error):
        if ctx.message.channel.id == Constants.PEFIPIC_CHANNEL_ID and isinstance(error, commands.CommandNotFound):
            await ctx.reply(embed=self.errorOnCommand(Constants.PEFI_PICTURE_COMMAND))
            return
        if ctx.message.channel.id in Constants.PEFIPRICE_CHANNEL_ID:
            return
        raise error

    def errorOnCommand(self, command):
        if command == Constants.PEFI_PICTURE_COMMAND:
            return discord.Embed(title="Error on command !",
                                 description=Constants.ERROR_ON_PEFIPIC,
                                 color=0xF24E4D)
