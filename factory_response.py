from __future__ import unicode_literals, annotations
from csv_instructions_parser import remove_blanks

check_list_goose = ["gooz", "gooze", "goos",
                    "gose", "goose", "guse",
                    "guuuse","guse"]


def return_factory_response(message: str) -> str:
    message = message.lower()
    message_args = message.split(' ')
    remove_blanks(message_args)
    if len(message_args) == 2 and message_args[0] == 'gooze':
        with open('chat_log.txt', 'a') as textfile:
            textfile.write(message + '\n')
        if message_args[1] == 'affection':
            return '*affectionate hoooooonk* *(Oh hoomin)*'
        elif message_args[1] == 'hiss':
            return '*The Gooze hisses back!*'
        elif message_args[1] == 'honk':
            return 'honk honk honk... honk ... honk honk ... honk honk'

    if check_start_contents_gooze(message):  # Is there an endwith thing?
        return 'Hiss!'
    elif check_goose_yeet(message):
        return 'Hoonnnnnnnkkkkkkkkkkkkkkkkkkkkkk!!!!!!!!!!!!!!'
    elif message == "good gooze":
        return "I luv u. <3"
    elif message.startswith("gooze died for our sins"):
        return "*The image of crucifixion floods your mind." + \
               " You are filled with sorrow...*"
    elif message.startswith("gooze, what do you say?"):
        return "*Honk!* \"Whatever you say! It's up to you.\""

    return ''


def compare_contents(message_content: str, target: List[str]) -> bool:
    """

    :param message_content: A string.
    :param target: A list of string to be checked against.
    :return: Returns whether one str in <target> exists in <message_content>

    Precondition: message_content is all in lower case and contains no spaces.
    The list <target> should not be modified.
    """
    for string in target:
        if string in message_content:
            return True
    return False


def check_if_at_least_one_in(message_content: str, *targets: List[str]) -> bool:
    """
    A function to check if as least one string each <targets> list exists in
    message_content.

    :param message_content: A string that represents the message content
    :param targets: A List of string. Multiple lists can be received.
    :return: Return whether at least one string in each list of string in
    <target> exists in message content. Boolean.
    """
    message_content = message_content.lower().replace(" ", "")
    for target in targets:
        if not compare_contents(message_content, target):
            return False
    return True


def create_all_combinations():
    """
    Hmmm... is it better to store these combinations somewhere at startup?
    Like combinations of yeet goose, and dum goose.
    :return:
    """


def check_start_contents_gooze(message_context: str):
    # Next plan = Check against various iterations of gooz
    check_list_dumb = ["dumb", "dum", "stupid", "vicious", "retarded", "sucks",
                       "suck", "horrible", "bad", "trash", "eatpoo", "poo"]
    # Read in a list of insults

    message_context = message_context.lower()
    message_context = message_context.replace(" ", "")

    for goose in check_list_goose:
        for dumb in check_list_dumb:
            if message_context.startswith(goose + dumb) or \
                    message_context.startswith(dumb + goose) or \
                    dumb in message_context and goose in message_context:
                return True
    return False


def check_goose_emoji(message_content: str):
    list_of_emojis = ["<:yeet:576183109293309962>",
                      "<:goose:576164231435517972>"]
    for emoji in list_of_emojis:
        if emoji not in message_content:
            return False
    return True


def check_goose_yeet(message_content: str):
    message_content = message_content.lower().replace(" ", "")
    if "yeet" in message_content:
        for goose in check_list_goose:
            if goose in message_content:
                return True
    return False
