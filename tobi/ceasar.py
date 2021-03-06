import os
import sys

def shift(letter, offset) :

    if not letter.isalpha() :
        return letter

    digit = ord(letter)
    base = 64 if digit < 91 else 96
    asc = base + (digit - base + offset) % 25

    return chr(asc)

def cipher(word, offset) :

    if offset <= 1 :
        return word

    result = ''

    for c in word :
        result += shift(c, offset)

    """Looks cooler."""
    #result = ''.join([shift(c, offset) for c in word])

    return str(result)

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :

    if (len(sys.argv) != 3) :
        error('Usage: python ceasar.py <string> <offset>')

    word = sys.argv[1]
    offset = sys.argv[2]

    if not offset.isdigit() :
        error('Offset has to be a number.')

    print(cipher(word, int(offset)))