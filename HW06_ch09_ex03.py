#!/usr/bin/env python3
# HW06_ch09_ex03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write forbidden_prompt and
#   - modify to create forbidden_param that accepts the string as an argument
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters: find_five
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports

# Body


def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return True
    return False


def forbidden_prompt():
    forbidden_string = input("Enter a string of forbidden letters: ")
    return forbidden_string

def forbidden_param():
    


def find_five():
    ...


##############################################################################
def main():
    ...
    # Your final submission should only call five_five

if __name__ == '__main__':
    main()
