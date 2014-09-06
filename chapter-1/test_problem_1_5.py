#!/usr/bin/env python

from problem_1_5 import *

def test_compress_abcd():
    assert compress('abcd') == 'abcd'

def test_compress_aaaabbbbcccdhhhhdddddd():
    assert compress('aaaabbbbcccdhhhhdddddd') == 'a4b4c3d1h4d6'

def test_compress_iiiiiiiijjiiiiiiii():
    assert compress('iiiiiiiijjiiiiiiii') == 'i8j2i8'

def test_compress_llllllllajdklllllll():
    assert compress('llllllllajdklllllll') == 'l8a1j1d1k1l7'

def test_compress_aabcccccaaa():
    assert compress('aabcccccaaa') == 'a2b1c5a3'

if __name__ == '__main__':
    test_compress_able()
    test_compress_backlog()
    test_compress_carbonized()
    test_compress_documentarily()
    test_compress_uncopyrightable()
