#!/usr/bin/env python3
# HW06_ch09_ex05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(word, req_letters):
	for letter in req_letters:
		if letter not in word:
			return False
	return True

def words_that_use(letters):
	fin = open('words.txt', 'r')
	words = fin.readlines()
	word_list = list()
	for word in words:
		if uses_all(word, letters):
			word_list.append(word)
	return word_list

##############################################################################
def main():
    all_vowels = words_that_use('aeiou')
    all_vowels_and_y = words_that_use('aeiouy')

    print("Number of words that use all aeiou: " + str(len(all_vowels)))

    print("Number of words that use all aeiouy: " + str(len(all_vowels_and_y)))




if __name__ == '__main__':
    main()
