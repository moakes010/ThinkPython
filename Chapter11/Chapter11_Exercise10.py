'''
Exercise 10  
Two words are “rotate pairs” if you can rotate one of them and get the other (see rotate_word in Exercise 12).
'''

import os

def rotate_pairs(word, word_dict):
    for i in range(1, 14):
        r = rotate_word(word, i)
        if r in word_dict:
            print(word, i, r)

def rotate_letter(letter, n):
    """Rotates a letter by n places.  Does not change other chars.

    letter: single-letter string
    n: int

    Returns: single-letter string
    """
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter) - start
    i = (c + n) % 26 + start
    return chr(i)

def rotate_word(word, n):
    """Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """
    res = ''
    for letter in word:
        res += rotate_letter(letter, n)
    return res

dword={}
cwd = os.getcwd()
for l in open(os.path.join(cwd, 'words.txt')):
    word = l.strip()
    dword[word] = word.lower()

for w in dword:
    rotate_pairs(w, dword)
