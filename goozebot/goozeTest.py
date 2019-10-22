from __future__ import unicode_literals
from dum import load_commands
import discord
from discord.ext.commands import Bot
from typing import Union, List, Dict
from flexible_input import *

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

my_bot = Bot(command_prefix=prefix, description=description)


# For context on async/await https://docs.python.org/3/library/asyncio-task.html


@my_bot.event
async def on_ready():
    print('logged in')
    print('discord version : ' + discord.__version__)
    game = discord.Activity(name='The Holy Goose Gospel', url=None,
                            type=2)
    # Types listed in help
    await my_bot.change_presence(activity=game, status=discord.Status.online)


load_commands(my_bot)


# Should maybe Create a general checking function for a given list of string
# against message content.
# Have "Check combos of one" and "check combos of two".

# Should use this for loading random data onto the bot
my_bot.randomdata = 1
print(my_bot.randomdata)
# Yeet

@my_bot.event
async def on_message(message):
    # print(message.content)
    # await cannot occur outside of async
    channel = message.channel
    if check_start_contents_gooze(
            message.content):  # Is there an endwith thing?
        await channel.send('Hiss!')
    elif check_goose_yeet(message.content):
        await channel.send('Hoonnnnnnnkkkkkkkkkkkkkkkkkkkkkk!!!!!!!!!!!!!!')
    elif message.content == "Good goose":
        await channel.send("I luv u. <3")
    elif message.content.startswith("Gooze died for our sins"):
        await channel.send("*The image of crucifixion floods your mind." +
                           " You are filled with sorrow...*")
    elif message.content.startswith("gooze, what do you say?"):
        await channel.send("*Honk!* \"Whatever you say! It's up to you.\"")
    else:
        await my_bot.process_commands(message)


my_bot.run(
    "NTczMzI4MTA4MzYzNzEwNTEy.XOjIrA.6eiBQT5y-kLb_e6EmR7XXxpLKI8")  # put a bot token here

# Permissions integer 207872
