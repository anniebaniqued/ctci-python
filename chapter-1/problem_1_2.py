#!/usr/bin/env python

# Problem Statement
# Implement a function void reverse(char* str) in C or C++ which reverses a
# null terminated string
#
# NOTE: For my personal case, I will simply be implementing a function that
# reverses any given string

def reverse(word):
    # Iterates through the string backwards and creates a reversed string
    retval = ''
    for i in range (len(word)-1, -1, -1):
        retval += word[i]
    return retval

def main():
    while(True):
        input_word = raw_input("Enter your word or hit 'q' to quit: ")
        if input_word == 'q':
            break
        print reverse(input_word)

if __name__ == '__main__':
    main()
