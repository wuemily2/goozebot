from __future__ import unicode_literals
import discord

from gooze_command_loader import load_commands
from discord.ext.commands import Bot
from typing import Union, List, Dict
from factory_response import *

# before you start, you must have the discord.py rewrite library installed. to do this, type the following to command prompt.
#
# python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite
#
# quick note, the discord.py library might have been integrated with the rewrite library at this moment in time,
# so if the above git repo throws an error, just try pip installing discord.py.
#
# if an error occurs that looks like 'no mudule named python3' then try replacing python3 with just python.
# of course, you need to have pip installed. after this is installed, you need to instantiate a bot as an actual member.
# use the following link in order to get your bot account set up.
#
# https://discordapp.com/developers/applications/me
#
# click new app, add a name to your bot and a profile picture (you don't need to add a description).
# when you create the app, scoll down to a button that says 'make user bot' or something like that and click it.
# after that, a new block on the page should open up that is labeled bot. click the 'click to reveal token' button.
# copy and paste that token into the my_bot.run("") line inbetween the quotation marks.
# now its up to you if you want to make the bot public. If it's your first bot then maybe don't select this.
# however if you intend to have this bot for public use, then select this.
# after all of that, you can finally begin coding your bot below.
# below is a website that gives the whole api refference for discord.py rewrite.
#
# https://discordpy.readthedocs.io/en/rewrite/api.html#
#
# this will tell you how to handle events and get objects you want. make sure to familiarize yourself with it.

prefix = 'gooze '
description = 'The Gooze stares menacingly'
category = "Gooze Calls"


class GoozeBot(Bot):
    def __init__(self, prefix_set, description_set):
        super().__init__(command_prefix=prefix_set, description=description_set)
        print("initialized")


my_bot = GoozeBot(prefix, description)


# For context on async/await https://docs.python.org/3/library/asyncio-task.html

# @my_bot.event
async def on_ready():
    print('logged in')
    print('discord version : ' + discord.__version__)
    game = discord.Activity(name='The Holy Goose Gospel', url=None,
                            type=2)
    # Types listed in help
    await my_bot.change_presence(activity=game, status=discord.Status.online)


my_bot.add_listener(on_ready)  # alternative to @my_bot.event

load_commands(my_bot)

"""
        if message.content.startswith("gooze"):
            await my_bot.fetch_user(397458781665230848).send(message.author.name +
                                       " said " + message.content)
                                       """


@my_bot.event
async def on_message(message):
    try:
        channel = message.channel
        factory_response = return_factory_response(message.content)
        if factory_response != '':
            await channel.send(factory_response)
        else:
            await my_bot.process_commands(message)
    except KeyError:
        await message.channel.send("please no animations")


my_bot.run(
    "NTczMzI4MTA4MzYzNzEwNTEy.XOjIrA.6eiBQT5y-kLb_e6EmR7XXxpLKI8")  # put a bot token here

# Permissions integer 207872
