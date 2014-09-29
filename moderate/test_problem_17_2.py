#!/usr/bin/env python

from problem_17_2 import *

def test_3x3_matrix_nobody_won():
    matrix = [[0, 0, 0],
              [1, 0, 2],
              [0, 1, 2]]
    assert has_won_3x3(matrix) == 0

def test_3x3_matrix_row_won():
    matrix = [[0, 0, 0],
              [1, 0, 2],
              [1, 1, 1]]
    assert has_won_3x3(matrix) == 1

def test_3x3_matrix_column_won():
    matrix = [[2, 1, 0],
              [2, 0, 2],
              [2, 1, 1]]
    assert has_won_3x3(matrix) == 2

def test_3x3_matrix_diagonal_won():
    matrix = [[1, 0, 0],
              [2, 1, 2],
              [2, 0, 1]]
    assert has_won_3x3(matrix) == 1

def test_5x5_matrix_nobody_won():
    matrix = [[0, 0, 0, 0, 0],
              [1, 0, 2, 0, 0],
              [0, 1, 2, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]]
    assert has_won_NxN(matrix, 5) == 0

def test_5x5_matrix_row_won():
    matrix = [[0, 2, 0, 0, 2],
              [1, 0, 2, 0, 0],
              [1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0],
              [0, 2, 0, 2, 0]]
    assert has_won_NxN(matrix, 5) == 1

def test_5x5_matrix_column_won():
    matrix = [[0, 0, 2, 0, 2],
              [1, 0, 2, 0, 0],
              [1, 0, 2, 1, 1],
              [0, 0, 2, 0, 0],
              [0, 1, 2, 0, 1]]
    assert has_won_NxN(matrix, 5) == 2

def test_5x5_matrix_diagonal_won():
    matrix = [[1, 0, 2, 0, 2],
              [1, 1, 2, 0, 0],
              [1, 0, 1, 1, 1],
              [0, 0, 2, 1, 0],
              [0, 1, 2, 0, 1]]
    assert has_won_NxN(matrix, 5) == 1

def test_5x5_matrix_reverse_diagonal_won():
    matrix = [[2, 0, 0, 0, 2],
              [1, 1, 0, 2, 0],
              [1, 0, 2, 1, 1],
              [0, 2, 0, 0, 0],
              [2, 1, 0, 0, 1]]
    assert has_won_NxN(matrix, 5) == 2
