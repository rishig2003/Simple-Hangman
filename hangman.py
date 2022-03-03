# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:35:27 2021

@author: Lenovo
"""

import random
from hangman_words import lst
word=random.choice(lst)
print(word)
y=[]
for l in word:
    y+='_'
print(y)
lives=6
c=False
while not c:
    guess=input('enter a letter: ').lower()
    if guess in y:
        print('letter already guessed')
    for i in range(len(word)):
        if guess==word[i]:
            y[i]=guess
            lives-=1
    print(y) 
    if guess not in word:
        print('letter not in the chosen word')
        lives-=1
        if lives==0:
            c=True
            print('YOU LOSE!!')

    if '_' not in y:
        c=True
        print('YOU WON!!')     
    