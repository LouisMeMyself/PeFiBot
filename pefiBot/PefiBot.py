import asyncio
import json
import typing
from datetime import datetime

import discord
from discord import NotFound
from discord.ext import commands

from constants import Constants, Channels
from pefiBot import PefiPic


class PefiBot:
    pefiPic_ = PefiPic.PefiPic()
    bot = commands.Bot
    channels = Channels.Channels

    def __init__(self, bot):
        self.bot = bot
        self.channels = Channels.Channels(bot)
        print(self.channels.profile_picture)

    async def on_ready(self):
        """starts pefibot"""
        print('pefiBot have logged in as {0.user}'.format(self.bot))

    async def pefipic(self, ctx):
        """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
        if ctx.message.guild.id in self.channels.profile_picture and ctx.message.channel.id == self.channels.profile_picture[ctx.message.guild.id].id:
            answer = self.pefiPic_.do_profile_picture(ctx.message.content)
            if len(answer) == 2:
                await ctx.reply(answer[0], file=answer[1])
            else:
                await ctx.reply(answer)
        return

    async def on_command_error(self, ctx, error):
        if ctx.message.channel.id == self.channels.profile_picture[ctx.message.guild.id].id and isinstance(error, commands.CommandNotFound):
            await ctx.reply(Constants.ERROR_ON_PEFIPIC)
            return
        raise error
