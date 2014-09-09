#!/usr/bin/env python

from problem_1_6 import *

def test_rotate_matrix_length_2():
    matrix = [[1,2], [3,4]]
    expected_matrix = [[3,1], [4,2]]
    rotate(matrix, 2)
    assert matrix == expected_matrix

def test_rotate_matrix_length_5():
    matrix = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]
    expected_matrix = [[1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3], [4,4,4,4,4], [5,5,5,5,5]]
    rotate(matrix, 5)
    assert matrix == expected_matrix

