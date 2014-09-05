#!/usr/bin/env python

# Problem Statement:
# Implement an algorithm to determine if a string has all unique characters.
# What if you can not use additional data structures?

def check_if_unique(word):
	# If length of the word is greater than 26, there MUST be a repetition
		if len(word) > 26:
			return False
	# Sort the letters and check if there's a repetition
	sorted_word = ''.join(sorted(word))
	for i in range (len(word)-1):
		if sorted_word[i] == sorted_word[i+1]:
			return False
	return True

def main():
	while(True):
		input_word = raw_input("Enter your word or hit 'q' to quit: ")
		if input_word == 'q':
			break
		print check_if_unique(input_word)

if __name__=='__main__':
	main()
