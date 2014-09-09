#!/usr/bin/env python

# Problem Statement
# Given an image represented by an NxN matrix, where each pixel in the image
# is 4 bytes, write a method to rotate the image by 90 degrees. Can you do
# this in place?

def rotate(matrix, n):
    layers = n/2
    length = n-1
    for layer in range(layers):
        for i in range(layer, length-layer):
            temp = matrix[layer][i]
            #Left -> Top
            matrix[layer][i] = matrix[length - i][layer]
            #Bottom -> left
            matrix[length - i][layer] = matrix[length - layer][length - i]
            #Right -> bottom
            matrix[length - layer][length - i] = matrix[i][length - layer]
            #Top -> Right
            matrix[i][length - layer] = temp