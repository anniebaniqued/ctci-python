#!/usr/bin/env python

# Problem Statement
# Implement a function void reverse(char* str) in C or C++ which reverses a
# null terminated string
#
# NOTE: For my personal case, I will simply be implementing a function that
# reverses any given string

def check_if_permutation(word1, word2):
    if len(word1) != len(word2):
        return False
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    for i in range (0, len(word1)):
        if sorted_word1[i] != sorted_word2[i]:
            return False
    return True

def main():
    while(True):
        input_word1 = raw_input("Enter your first word or hit 'q' to quit: ")
        if input_word1 == 'q':
            break
        input_word2 = raw_input("Enter your second word or hit 'q' to quit: ")
        if input_word2 == 'q':
            break
        print check_if_permutation(input_word1, input_word2)

if __name__ == '__main__':
    main()
