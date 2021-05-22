import asyncio
import typing
import discord
from discord.ext.commands import has_permissions
import Constants
from Pefibot import Pefibot
from discord.ext import commands


# intents = discord.Intents.default()
# intents.members = True

# bot = commands.Bot(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!')
pefibot = Pefibot


@bot.event
async def on_ready():
    """starts pefibot"""
    global pefibot
    pefibot = Pefibot(bot)


@bot.command()
async def pefipic(ctx):
    """command for personalised profile picture, input a color (RGB or HEX) output a reply with the profile picture"""
    if ctx.message.channel.id == pefibot.pefipic.bot_channel[ctx.message.guild.id].id:
        answer = pefibot.do_profile_picture(ctx.message.content)
        if len(answer) == 2:
            await ctx.reply(answer[0], file=answer[1])
        else:
            await ctx.reply(answer)
        return


# @bot.event
# async def on_raw_reaction_add(payload):
#     """Add penguin role when a penguin reaciton is added on a particular message (not a message from pefibot or a reaction of pefibot)"""
#     if payload.user_id == bot.user.id:  # check if user that reacted is not pefibot
#         return
#     if payload.message_id == bot.user.id:  # check if message is not from pefibot
#         return
#     if pefibot.pefireact.bot_channel[payload.guild_id].id == payload.channel_id and payload.message_id == 839659452411674645 and payload.emoji.name == '\N{PENGUIN}':
#         member = payload.member
#         role = discord.utils.get(member.guild.roles, name="Penguin")
#         await member.add_roles(role)
#     return


# @bot.event
# async def on_raw_reaction_remove(payload):
#     """harder to remove than add a role, to do"""
#     if payload.user_id == bot.user.id:  # check if user that reacted is not pefibot
#         return
#     if payload.message_id == bot.user.id:  # check if message is not from pefibot
#         return
#     if pefibot.pefireact.bot_channel[payload.guild_id].id == payload.channel_id and payload.message_id == 839659452411674645 and payload.emoji.name == '\N{PENGUIN}':
#         member = payload.member
#         role = discord.utils.get(member.guild.roles, name="Penguin")
#         await member.remove_roles(role)
#     return


# @bot.command()
# @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
# async def ban(ctx, members: commands.Greedy[discord.Member],
#               delete_days: typing.Optional[int] = 0, *,
#               reason: str):
#     """Mass bans members with an optional delete_days parameter, send a message before banning people to be sure it's not a mistake"""
#     if (ctx.channel.name == Constants.PEFIPIC_CHANNEL_NAME):  # to change to an id / channel not a name
#         accept_decline = await ctx.send("Banning {}".format(" ".join([member.mention for member in members])))
#         await accept_decline.add_reaction("✅")
#         await accept_decline.add_reaction("❌")
#
#         def check(reaction, user):
#             return user == ctx.message.author and (str(reaction.emoji) == '✅' or str(reaction.emoji) == '❌')
#
#         try:
#             reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
#         except asyncio.TimeoutError:
#             await accept_decline.delete()
#             await ctx.send('Timed out')
#         else:
#             await accept_decline.delete()
#             if reaction.emoji == "✅":
#                 for member in members:
#                     a = 1
#                     # await member.ban(delete_message_days=delete_days, reason=reason)
#                 if delete_days is not None:
#                     await ctx.send(
#                         "Banned {} for {} days for {}".format(" ".join([member.mention for member in members]),
#                                                               delete_days, reason))
#                 else:
#                     await ctx.send("Banned {} forever, for {}".format(" ".join([member.mention for member in members]),
#                                                                       delete_days, reason))
#             else:
#                 await ctx.send("Bans canceled")


if __name__ == '__main__':
    with open(".key", "r") as f:
        key = f.read().replace("\n", "")
    bot.run(key)
