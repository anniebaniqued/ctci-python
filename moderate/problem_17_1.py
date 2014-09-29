#!/usr/bin/env python

# Problem Statement:
# Write a function to swap a number in place (that is, without temporary
# variables)

def swap(a, b):
    # For example if a = 5 and b = 3
    a = a-b # a-b = 5-3 = 2
    b = a+b # a+b = 2+3 = 5
    a = b-a # b-a = 5-2 = 3

    print ("a = %s, b = %s") % (a,b)
    return (a, b)
