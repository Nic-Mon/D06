#!/usr/bin/env python3
# HW06_ch09_ex02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
#   - name your function print_no_e
##############################################################################
# Imports

# Body
def has_no_e(word):
	for letter in word:
		if letter == 'e' or letter == 'E':
			return False
	return True

def print_no_e():
	fin = open('words.txt', 'r')
	words = fin.readlines()
	count = 0
	total = 0
	print("Words with no e:")
	for word in words:
		total += 1
		if has_no_e(word.strip()):
			print(word.strip())
			count += 1
	print("Percentage of words with no e: " + str(count/total) + "%")


##############################################################################
def main():

	print(has_no_e("Hello"))
	print(has_no_e("Edward"))
	print(has_no_e("Nicolas"))
	print(has_no_e("Mon"))

	print_no_e()


if __name__ == '__main__':
    main()
