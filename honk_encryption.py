from typing import List, Iterator


class HonkLanguage:
    pass  # Used to specify different Honk keys


HONKMAP = {'h': 0, 'H': 1, 'o': 0, 'O': 1, 'n': 0, 'N': 1, 'k': 0, 'K': 1}
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphakey = {}
for i in range(26):
    alphakey[i + 1] = alphabet[i]  # Map Decimals to letters

rev_alphakey = {}
for key in alphakey:  # Map letters to numbers
    rev_alphakey[alphakey[key]] = key

neutral_honk = "honk"
END_OF_WORD = "knoh"


### Convert Honks to a message

def _honk_to_decimal(honks: str) -> int:
    """
    Precondition: correct Honks
    :param honks: a string denoting honks
    :return: A decimal value
    """
    sum = 0
    for i in range(1, len(honks) + 1):
        char = honks[-i]
        power = 2 ** (i - 1)
        sum += HONKMAP[char] * power
    return sum


def _honk_to_letter(honks: str) -> str:
    """
    Takes a honk string and converts it to the corresponding letter
    :param honks:
    :return:
    """
    return alphakey[_honk_to_decimal(honks)]


def _honks_to_word(honks: str) -> str:
    """
    Takes a set of honks representing a word, and converts it to a word.
    :param honks:
    :return:
    """
    honk_list = list(map(str.strip, honks.split(" ")))
    #print(honk_list +  [" yo"])
    word = ""
    for honk in honk_list:
        if len(honk) in (4,8):
            word = word + _honk_to_letter(honk)
    return word


def honks_to_words(honks: str) -> str:
    """
    Takes a set of honks representing sentences, and converts it to sentences.
    :param honks:
    :return:
    """

    honk_words = _splice_honks(honks)
    #print(honk_words)
    sentence = ""
    for enc_word in honk_words:
        sentence = sentence + _honks_to_word(enc_word) + " "
    #print(sentence)
    return sentence


def _splice_honks(honks: str) -> List[str]:
    """
    Splice honks string based on encryption key.
    :param honks:
    :return: An iterator,  iterates through each word
    """
    words = honks.split(END_OF_WORD)
    return list(map(str.strip, words))


### Convert your message to Honks

def _letter_to_binary(letter: str) -> str:
    """
    Takes a letter and convert it to its mapped binary value
    :param letter: a character
    :return: a binary string representing the letter



    """
    number = rev_alphakey[letter]
    binary_str = str(bin(number))[2:]
    return binary_str


bin_to_honk_map = {1: {'0': 'k', '1': 'K'},
                   3: {'0': 'o', '1': 'O'},
                   2: {'0': 'n', '1': 'N'},
                   4: {'0': 'h', '1': 'H'}}


##
def _bin_to_honk(bin_inc_honk: str) -> str:
    """
    :param inc_honk: binary string of length 4 or less
    :return:

    >>> _bin_to_honk("1000")
    'Honk'
    >>> _bin_to_honk("0001")
    'honK'

    """
    acc = ""
    for i in range(1, len(bin_inc_honk) + 1):
        acc = bin_to_honk_map[i][bin_inc_honk[-i]] + acc
    return acc


def _binary_to_honk(bin_incomplete_honk: str) -> str:
    """

    :param bin_incomplete_honk: binary string of up to length 8
    :return: Corresponding honk letters.

    >>>

    """
    if len(bin_incomplete_honk) == 0:
        return ""
    honk_piece1 = bin_incomplete_honk[:-4]
    honk_piece2 = bin_incomplete_honk[-4:]
    #print(honk_piece1)
    #print(honk_piece2)
    return _bin_to_honk(honk_piece1) + _bin_to_honk(honk_piece2)


def _bin_to_honk_w_fill(bin_incomplete_honk: str) -> str:
    """

    :param bin_incomplete_honk: a binary string representing a letter.
    :return: the correct corresponding honks
    """
    honk_piece = ""
    if len(bin_incomplete_honk) < 4:  # 0 to 3
        need = 4 - len(bin_incomplete_honk)
        honk_piece = neutral_honk[:need]
        #print(honk_piece)
    elif 4 < len(bin_incomplete_honk) < 8:
        need = 8 - len(bin_incomplete_honk)
        honk_piece = neutral_honk[:need]
        #print(honk_piece)
    rest_of_honk =  _binary_to_honk(bin_incomplete_honk)
    #print(rest_of_honk)
    return honk_piece + _binary_to_honk(bin_incomplete_honk)


def letter_to_honk(letter: str) -> str:
    return _bin_to_honk_w_fill(_letter_to_binary(letter))


def word_to_honk(word: str) -> str:
    acc = ""
    for char in word:
        acc += letter_to_honk(char) + " "
    acc += END_OF_WORD
    return acc


def words_to_honk(words: str) -> str:
    """

    :param words: words, lowercase only and no punctuation
    :return:
    """
    words = list(map(str.strip, words.split(" ")))
    honk_str = ""
    for word in words:
        honk_str += word_to_honk(word) + " "
    return honk_str


##


if __name__ == "__main__":
    #print(_honk_to_decimal("HONKHONK"))
    #print(_honk_to_letter("honK") +
    #      " " + _honk_to_letter("hoNK") + _honk_to_letter("honkHONK")
    #      + _honk_to_letter("honKhONK"))
    # print(letter_to_honk("z"))
    #print(letter_to_honk("a"))
    #print(letter_to_honk("z"))

    print(words_to_honk("cow piss"))
    print(honks_to_words(words_to_honk("cow piss")))
    print(honks_to_words(words_to_honk("how is life my friends")))
    print(words_to_honk("am fine the c videos for two oh nine are super boring though"))
