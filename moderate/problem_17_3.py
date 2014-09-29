#!/usr/bin/env python

# Problem Statement:
# Write an algorithm which computes the number of trailng zeros in n factorial

def countFactZeroes(num):
    count = 0
    i = 5
    
    if num < 0:
        return -1

    while num/i > 0:
        count += num/i
        i = i*5

    return count