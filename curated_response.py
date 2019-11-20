from __future__ import unicode_literals, annotations
from discord.ext import commands
import random
import asyncio

def test_write(user_id: str):
    with open(user_id + '.txt','a') as file:
        file.write("test successful")

@commands.command(name='bless')
async def bless(context):
    pass


@commands.command(name='pet')
async def pet(context):
    await context.message.channel.send("You pet the goose...")
    #test_write(str(context.message.author.id))
    await asyncio.sleep(2)



@commands.command(name='glare')
async def glare(context):
    await context.message.channel.send("...")
    await asyncio.sleep(2)
    text = '*The Gooze Attacks! It\'s hard to fend them off.*'
    await context.message.channel.send(text)


@commands.command(name='approach')
async def approach(
        context):
    await context.message.channel.send("...")
    await asyncio.sleep(2)
    text = ['*The Gooze starts honking*',
            "*THE GOOZE BITES AND BEATS ITS WINGS*"]
    text = text[0] if random.randint(0, 3) % 2 == 1 else text[1]
    await context.message.channel.send(text)


@commands.command(name='i_talk')
async def i_talk(context):
    text = ['HONK', "\"Leave Hoomin\""]
    text = text[0] if random.randint(0, 3) % 2 == 1 else text[1]
    await context.message.channel.send(text)


@commands.command(name='san')
async def san(context, *args):
    y = random.randint(0, len(args) - 1)
    text = args[y]
    await context.message.channel.send("Honk..." + "(" + text + "?)")


def load_curated_gooze_response(bot: discord.ext.commands.Bot):
    bot.add_command(pet)
    bot.add_command(glare)
    bot.add_command(approach)
    bot.add_command(i_talk)
    bot.add_command(san)

