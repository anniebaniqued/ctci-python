#!/usr/bin/env python

# Problem Statement
# Given two strings write a method to decide if one is a permutation of the
# other

def check_if_permutation(word1, word2):
    # If the length of the words are not the same, it is impossible for one
    # to be a permutation of the other
    if len(word1) != len(word2):
        return False

    # Sorts both words and checks if equal
    sorted_word1 = ''.join(sorted(word1))
    sorted_word2 = ''.join(sorted(word2))
    return sorted_word1 == sorted_word2

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
