#!/usr/bin/env python3

import random
# Script for showing random words for mmemonics training
"""
infile = open("slowa.txt", "r")
words_list = infile.readlines()
infile.close()
picked_words = []
for i in range(22):
    picked_words.append(random.choice(words_list))

for i,word in enumerate(picked_words):
    print("{}. {}".format(i+1, word), end="")
"""


def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds

slowa_words = load_words_from_file("words.txt")
picked_words = []

count = 0
while count < 22:
    word = random.choice(slowa_words)
    if len(word) > 7:
        picked_words.append(word)
        count += 1

for i,word in enumerate(picked_words):
    print("{}. {}".format(i+1, word))

print()
print()



