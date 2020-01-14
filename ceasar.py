import os
import sys

def shift(letter, offset) :

    digit = ord(letter)
    base = 64 if digit < 91 else 96
    shift = (digit - base + offset) % 25

    return chr(base + shift)

def cipher(word, offset) :

    if offset <= 1 :
        return word

    result = ''

    for c in word :
        if not c.isalpha() :
            error(c + ' is not alphabetic!')

        result = result + shift(c, offset)

    """Looks cooler but requires c.isalpha() in shift(...) instead."""
    #result = ''.join([shift(c, offset) for c in word])

    return str(result)

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :

    if (len(sys.argv) != 3) :
        error('Usage: python ceasar.py <string> <offset>')

    word = sys.argv[1]
    offset = int(sys.argv[2])

    if not isinstance(offset, int) :
        error('Offset has to be a number.')

    print(cipher(word, offset))