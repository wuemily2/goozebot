from __future__ import unicode_literals, annotations
import discord
from discord.ext.commands import Bot
import random
import asyncio


def load_dm_capabilities(bot: Bot) -> str:
    help_string = "The Messenger Goose: \n"
    '''
    command = ("timed_message", "Send a timed message with 'gooze " +
               "timed_message <user_mention or id> " +
               " <repeats> <seconds between repeats>" +
               " <message>'. Please don't abuse this.")

    @bot.command(name=command[0], help=command[1])
    async def timed_message(context, victim: discord.Member, repeats: int = 1,
                            interval: int = 0, *args):
        # Note: Can make victim of type "Member" or "User".
        # It doesn't seem to matter.

        try:
            while repeats >= 1:
                repeats -= 1
                await victim.send(" ".join(args))
                await context.message.channel.send("1 message Sent to "
                                                   + victim.name)
                await asyncio.sleep(interval)
            await context.message.channel.send("All messages Sent to "
                                               + victim.name)
        except:
            await context.message.channel.send("Failed to send message.")
            return None
    
    help_string += "\t" + ": ".join(command) + "\n"
    '''
    command = ("message", "Send a message with 'gooze " +
               "message <user_mention or id> <yourmessage>")

    @bot.command(name=command[0], help=command[1])
    async def message(context, victim: discord.User, *args):

        try:
            await victim.send(" ".join(args))
            await context.message.channel.send("Message Sent to "
                                               + victim.name)
        except:
            await context.message.channel.send("Failed to send message.")
            return None

    help_string += "\t" + ": ".join(command) + "\n"
    '''
    @timed_message.error
    @message.error
    async def timed_message_error(ctx, error):
        # This might need to be (error, ctx), I'm not sure
        if isinstance(error, discord.ext.commands.errors.BadArgument):
            await ctx.message.channel.send('I could not find that user.')
    '''
    command = ("curse", "When you want to damn it all.")

    @bot.command(name=command[0], help=command[1])
    async def curse(context, arg: str):
        if arg == "me":
            await context.message.channel.send("You foul hoomin.")
        elif arg == "everything" or arg == "all":
            await context.message.channel.send(
                "'Damn it all! Just, damn it all!'")
        elif arg == "everyone":
            await context.message.channel.send("I hate you all and I just want"
                                               + " to disappear!")
        elif arg == "you":
            await context.message.channel.send("*The Gooze glares menacingly.*")
        else:
            await context.message.channel.send("Die in hell, " + arg)

    help_string += "\t" + ": ".join(command) + "\n"

    command = ("remote", "when you want to send a remote message")

    @bot.command(name = command[0], help=command[1])
    async def remote(context, channeru: discord.TextChannel, *args):
        try:
            await channeru.send(" ".join(args))
            await context.message.channel.send("Message sent on " + channeru.name)
        except:
            await context.message.channel.send("Failed to send message.")

    help_string += "\t" + ": ".join(command) + "\n"

    command = ("tell", "When you want to gooze to tell someone" +
                       " to do something for you")

    @bot.command(name=command[0], help=command[1])
    async def tell(context, victim, *args):
        try:
            if "study" in args[0:2]:
                await context.message.channel.send("GO STUDY," + victim + "!!!")
                try:
                    victim = (discord.User)(victim)
                    await victim.send("Honk! Please Study!")
                except:
                    await context.message.channel.send(":(")
            else:
                await context.message.channel.send("I'm not sure what to honk.")
        except:
            await context.message.channel.send(
                "Failed to tell anyone anything.")
        await context.message.delete()

    return help_string
