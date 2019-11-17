from __future__ import unicode_literals, annotations
from csv_instructions_parser import *
from admin_commands import load_admin_commands
from curated_response import load_curated_gooze_response
from user_dm import load_dm_capabilities
from discord.ext.commands import Bot


def load_commands(bot: Bot):
    bot.remove_command('help')  # Removes the existing help command.
    load_admin_commands(bot,
                        "I work and speak only for my MASTER!",
                        "Goozebot")
    load_curated_gooze_response(bot)
    load_dm_capabilities(bot)

    gooze_command_info = read_cmd_file('command_help_doc.csv')
    gooze_messaging_info = read_cmd_file('messaging_commands.csv')
    gooze_simple = read_cmd_file('simple_commands.csv')
    gooze_admin = read_cmd_file('admin_commands.csv')

    @bot.command(passcontext=True, name="help")
    # This is a help message called with calls
    async def help(context):
        # you can make any command you want,
        # this is just a command to display a command list
        message = gooze_command_info
        await context.message.channel.send(message)

    @bot.command(passcontext=True, name="simple")
    async def simple(context):
        await context.message.channel.send(gooze_simple)

    @bot.command(passcontext=True, name="messenger")
    async def messenger(context):
        await context.message.channel.send(gooze_messaging_info)

    @bot.command(passcontext=True, name="admin_commands")
    async def admin_commands(context):
        await context.message.channel.send(gooze_admin)
