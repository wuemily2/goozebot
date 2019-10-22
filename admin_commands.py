from __future__ import unicode_literals, annotations
import discord
from discord.ext.commands import Bot
import random
import asyncio

admins = []


def load_admin_commands(bot: Bot, fixed_response: str, name: str) -> str:
    # fixed response = "I work and speak only for my MASTER!"

    # ==== Say Command ====
    help_string = "Admin Commands: \n"

    command = ("say", name + " says what you say. (admin)")

    global admins

    @bot.command(name=command[0], help=command[1])
    async def say(context, *args):
        if context.message.author.id in admins:
            channeru = context.message.channel
            await context.message.delete()
            await channeru.send(" ".join(args))

        else:
            await context.message.channel.send("...")
            await asyncio.sleep(3)
            await context.message.channel.send(fixed_response)

    help_string += "\t" + ": ".join(command) + "\n"

    command = ("bite", "The " + name + " bites the target.")

    @bot.command(name=command[0], help=command[1])
    async def bit(context, arg: str):
        if context.message.author.id in admins:
            await context.message.channel.send("*The Goose Bites " + arg + "," +
                                               " die heathen!*")
        else:
            await context.message.channel.send("...")
            await asyncio.sleep(3)
            await context.message.channel.send("*The Goose bites " +
                                               context.message.author.name +
                                               " instead!*")

    help_string += "\t" + ": ".join(command) + "\n"

    command = ("admin", "Emily can grant admin.")

    @bot.command(name=command[0], help=command[1])
    async def admin(context, target: discord.User):
        if context.message.author.id == 397458781665230848:
            if target.id not in admins:
                admins.append(target.id)
                await context.message.channel.send("Successfully granted " +
                                                   target.name
                                                   + " admin for this session.")
            else:
                await context.message.channel.send(target.name +
                                                   " is already registered.")

    help_string += "\t" + ": ".join(command) + "\n"

    command = ("remove_admin", "Emily can remove admin.")

    @bot.command(name=command[0], help=command[1])
    async def remove_admin(context, target: discord.User):
        if context.message.author.id == 397458781665230848:
            if target.id in admins:
                admins.remove(target.id)
                await context.message.channel.send("Successfully removed " +
                                                   target.name
                                                   + " admin for this session.")
            else:
                await context.message.channel.send(target.name +
                                                   " is not admin.")

    help_string += "\t" + ": ".join(command) + "\n"

    return help_string
