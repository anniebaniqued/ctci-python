#!/usr/bin/env python

from problem_17_3 import *

def test_countFactZeroes_2():
    assert countFactZeroes(2) == 0

def test_countFactZeroes_5():
    assert countFactZeroes(5) == 1

def test_countFactZeroes_30():
    assert countFactZeroes(30) == 7

def test_countFactZeroes_60():
    assert countFactZeroes(60) == 14