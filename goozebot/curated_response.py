from __future__ import unicode_literals, annotations
import discord
from discord.ext.commands import Bot
import random
import asyncio


def load_curated_gooze_response(bot: Bot) -> str:
    help_string = "Interact with Gooze: \n"

    # ==== affection Command ====
    command = ("affection", "You show the goose some affection.")

    @bot.command(name=command[0], help=command[1])
    async def affection(context):
        text = '*affectionate hoooooonk* *(Oh hoomin)*'
        await context.message.channel.send(text)

    help_string += "\t" + ": ".join(command) + "\n"

    # ==== hiss Command ====
    command = ("hiss", "Dumb gooze hiss back.")

    @bot.command(name=command[0], help=command[1])
    async def hiss(
            context):
        text = 'Hiss!'
        await context.message.channel.send(text)

    help_string += "\t" + ": ".join(command) + "\n"

    # ==== glare Command ====
    command = ("glare", "Stare at the goose.")

    @bot.command(name=command[0], help=command[1])
    async def glare(
            context):
        await context.message.channel.send("...")
        await asyncio.sleep(2)
        text = '*The Gooze Attacks! It\'s hard to fend them off.*'
        await context.message.channel.send(text)

    help_string += "\t" + ": ".join(command) + "\n"
    # ==== approach Command ====
    command = ("approach", "approach the gooze")

    @bot.command(name=command[0], help=command[1])
    async def approach(
            context):
        await context.message.channel.send("...")
        await asyncio.sleep(2)
        text = ['*The Gooze starts honking*',
                "*THE GOOZE BITES AND BEATS ITS WINGS*"]
        text = text[0] if random.randint(0, 3) % 2 == 1 else text[1]
        await context.message.channel.send(text)

    help_string += "\t" + ": ".join(command) + "\n"
    # ==== i_talk Command ====
    command = ("i_talk", "You talk to the Gooze, you haven't done this before" +
               " have you?")

    @bot.command(name=command[0], help=command[1])
    async def i_talk(
            context):
        text = ['HONK', "\"Leave Hoomin\""]
        text = text[0] if random.randint(0, 3) % 2 == 1 else text[1]
        await context.message.channel.send(text)

    help_string += "\t" + ": ".join(command) + "\n"
    # ==== -san Command ====
    command = ("-san", "You can write more words to the goose," +
               " since you treat em with respect." +
               "\n Address gooze with san and he shall listen.")

    @bot.command(name=command[0], help=command[1])
    async def san(context, *args):
        y = random.randint(0, len(args) - 1)
        text = args[y]
        await context.message.channel.send("Honk..." + "(" + text + "?)")

    help_string += "\t" + ": ".join(command) + "\n"

    # ========= Defunct Commands =========

    # ==== yeet Command ====
    command = ("yeet", "You yeet the goose")

    @bot.command(name=command[0], help=command[1])
    async def yeet(context):  # Doesn't run because of current on_message
        text = "!!!!!!!!!!!!!!!!!!!!!!!!!"
        await context.message.channel.send(text)

    help_string += "\t" + ": ".join(command) + "\n"

    # ==== dum Command ====
    command = ("dum", "You insult the goose.")

    @bot.command(name=command[0], help=command[1])
    # Doesn't run because of current on_message
    async def dum(context):
        text = 'Hiss!'
        await context.message.channel.send(text)

    help_string += "\t" + ": ".join(command) + "\n"

    return help_string
