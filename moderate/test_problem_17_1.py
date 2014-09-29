#!/usr/bin/env python

from problem_17_1 import *

def test_swap_one():
    assert swap(5,3) == (3,5)

def test_swap_two():
    assert swap(-1,-15) == (-15,-1)

def test_swap_three():
    assert swap(90,-13) == (-13,90)