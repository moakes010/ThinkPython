'''
Exercise 12  
Two words are a reverse pair if each is the reverse of the other. Write a program that finds all the 
reverse pairs in the word list.
'''

word_list = ['the', 'brown', 'dog', 'ran', 'down', 'street']
word = 'god'

def rev_pair(lword, word):
    rev_word = word[::-1]
    if rev_word in lword:
        return True

def main():
    if rev_pair(word_list, word):
        print("Reverse pair: " + word, word[::-1])
    else:
        print("No reverse pair")
main()