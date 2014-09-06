#!/usr/bin/env python

from problem_1_1 import *

def test_check_if_unique_able():
    assert check_if_unique('able') == True

def test_check_if_unique_backlog():
    assert check_if_unique('backlog') == True

def test_check_if_unique_carbonized():
    assert check_if_unique('carbonized') == True

def test_check_if_unique_documentarily():
    assert check_if_unique('documentarily') == True

def test_check_if_unique_uncopyrightable():
    assert check_if_unique('uncopyrightable') == True

def test_check_if_unique_ball():
    assert check_if_unique('ball') == False

def test_check_if_unique_pokemon():
    assert check_if_unique('pokemon') == False

def test_check_if_unique_abhorrence():
    assert check_if_unique('abhorrence') == False

def test_check_if_unique_pianistically():
    assert check_if_unique('pianistically') == False

def test_check_if_unique_pyroelectricities():
    assert check_if_unique('pyroelectricities') == False

if __name__ == '__main__':
    test_check_if_unique_able()