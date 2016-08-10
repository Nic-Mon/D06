#!/usr/bin/env python
# HW06_ch09_ex04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1: loco focal fool
#       2: aloha alcohol
#       3: fell off of alfalfa
##############################################################################
# Imports

# Body
def uses_only(word, letters):
	for letter in word:
		if letter not in letters:
			return False
	return True

def words_use_only(letters):
	fin = open('words.txt', 'r')
	words = fin.readlines()
	for word in words:
		if uses_only(word.strip(), letters):
			print(word.strip())

##############################################################################
def main():
    
    print("Words that use only acefhlo: ")
    words_use_only('acefhlo')

if __name__ == '__main__':
    main()
