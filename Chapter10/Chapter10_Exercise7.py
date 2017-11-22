'''
Chapter 10 Exercise 7  
Two words are anagrams if you can rearrange the letters from one to spell the other. 
Write a function called is_anagram that takes two strings and returns True if they are anagrams
'''

word1='DoctorWho'
word2='Torchwood'

def is_anagram(s1, s2):
    if len(s1) == len(s2):
        s1_list = [ i for i in s1.lower() ]
        s2_list = [ j for j in s2.lower() ]
        return (s1_list.sort() == s2_list.sort())
 

print(is_anagram(word1, word2))