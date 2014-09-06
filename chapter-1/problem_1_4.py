#!/usr/bin/env python

# Problem Statement:
# Write a method to replace all spaces in a astring with '%20'. You may assume
# that the string has sufficient space at the end of the string to hold the
# additional characters, and that you are given the "true" length of the
# string. (Note: if implementing in Java, please use a character array so that
# you can perform this operation in place).
#
# EXAMPLE
#
# Input : "Mr John Smith    "
# Output: "Mr%20John%20Smith"

def replace_spaces(word):
    word = word.strip()
    word = word.replace(' ', '%20')
    return word

def main():
    while(True):
        input_word = raw_input("Enter your word or hit 'q' to quit: ")
        if input_word == 'q':
            break
        print replace_spaces(input_word)

if __name__ == '__main__':
    main()
