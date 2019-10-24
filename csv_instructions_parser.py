from __future__ import unicode_literals, annotations
from typing import List
import csv


def remove_element(a: List[str], target: str) -> None:
    while target in a:
        a.remove(target)


def remove_blanks(a: List[str]) -> None:
    remove_element(a, '')


def read_cmd_file(filename: str) -> str:
    with open(filename, 'r') as command_file:
        line_parser = csv.reader(command_file)
        output = ''
        for words in line_parser:
            remove_blanks(words)
            output = ('\t' + output + ": ".join(words[1:])) \
                if (len(words) > 0 and words[0] == '?') \
                else output + ": ".join(words)
            output = output + "\n"
        return output
