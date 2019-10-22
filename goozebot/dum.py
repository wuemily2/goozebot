from __future__ import unicode_literals, annotations
from admin_commands import load_admin_commands
from curated_response import load_curated_gooze_response
from user_dm import load_dm_capabilities

import discord
from discord.ext.commands import Bot
import random
import asyncio


def load_commands(bot: Bot):
    bot.remove_command('help')  # Removes the existing help command.
    admin_help = load_admin_commands(bot,
                                     "I work and speak only for my MASTER!",
                                     "Goozebot")
    gooze_response_help = load_curated_gooze_response(bot)
    dm_help = load_dm_capabilities(bot)

    # I want to try making something where I don't remove it though.

    # https://discordpy.readthedocs.io/en/latest/faq.html#what-is-a-coroutine

    @bot.command(passcontext=True, name="help")
    # This is a help message called with calls
    async def help(
            context):  # you can make any command you want, this is just a command to display a command list
        message = ('```' +
                   "===== Gooze Commands ===== \n"
                   + "You can use all commands with 'gooze <command name>"
                   + " <any parameters required>' \n"
                   +
                   gooze_response_help +
                   dm_help +
                   admin_help +
                   '```')
        await context.message.channel.send(message)
