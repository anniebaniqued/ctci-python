#!/usr/bin/env python

# Problem Statement
# Implement a method to perform a basic string compression using the counts
# of the repeated characters. For example, the string aabcccccaaa would become
# a2b1c5a3. If the "compressed" string would not become smaller than the
# original string, your method should return the original string.

def compress(word):
    retval = ''
    prev = ''
    counter = 1
    # Check if previous character is the same as current character. If so,
    # incement counter. If not, add previous character and it's counter to
    # the retval. At the end print last character and it's counter.
    for i in range (1,len(word)):
        prev = word[i-1]
        if word[i] == prev:
            counter += 1
        else:
            retval += prev
            retval += str(counter)
            prev = word[i]
            counter = 1
    retval += prev
    retval += str(counter)
    if len(retval) < len(word):
        return retval
    else:
        return word

def main():
    while(True):
        input_word = raw_input("Enter your word or hit 'q' to quit: ")
        if input_word == 'q':
            break
        print compress(input_word)

if __name__ == '__main__':
    main()
