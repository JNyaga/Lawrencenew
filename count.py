from words import words
from collections import Counter

# W = [word for word in words if word[0] == 'w' or word[0] == 'W']
# print(len(W))
# print(Counter(W))
word = input('guess a word that can be in the list:\n')
if word in words:
    print('yeah its there')
else:
    print('NOP')
