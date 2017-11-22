import re

def most_frequent(s):
    '''
    print letters in decreasing order of text
    '''
    count={}
    #Obliterate everything by word and number characters then count letters
    new_s = re.sub(ur'[^\w\d]+', '', s.lower())
    for letter in new_s:
        count[letter] = count.setdefault(letter, 0) + 1
    
    #Create list of tuples that contain (letter, letter frequency)
    letters=[]
    for l, f in count.iteritems():
        letters.append((l, f))
    
    #reverse sort list of tuples and create new list with only letter
    ordered = [ i[0] for i in sorted(letters, key=lambda freq: freq[1], reverse=True) ]
    return ordered

passages = ['passage_english.txt', 'passage_french.txt', 'passage_german.txt']

for f in passages:
    with open(f, 'r') as passage:
        p=passage.read()
        print(most_frequent(p))

'''
Expected Results according to https://en.wikipedia.org/wiki/Letter_frequency

Text from Ethan Frome by Edith Wharton

When I had been there a little longer, and had seen this phase of crystal clearness followed by long stretches of sunless cold; 
when the storms of February had pitched their white tents about the devoted village and the wild cavalry of March winds had charged 
down to their support; I began to understand why Starkfield emerged from its six months’ siege like a starved garrison capitulating 
without quarter

Used https://translate.google.com to translate to French and German

Expected Relative Frequency of letters (Top 5)

English [e, t, a, o, i]
French [e, s, a, i. t ]
German [e, n, s, r, i ]

Observed 
['e', 't', 'a', 's', 'r', 'h', 'd', 'i', 'o', 'n', 'l', 'c', 'g', 'w', 'f', 'u', 'b', 'm', 'p', 'y', 'v', 'k', 'q', 'x']
['e', 's', 'a', 'u', 'i', 'n', 't', 'r', 'd', 'l', 'o', 'm', 'v', 'c', 'g', 'p', 'f', 'q', 'j', 'h', 'b', 'k', 'y', 'x']
['e', 'n', 'a', 'r', 't', 'i', 's', 'g', 'l', 'h', 'd', 'u', 'o', 'w', 'c', 'f', 'b', 'k', 'v', 'z', 'm', 'p']

'''
