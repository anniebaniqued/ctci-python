#!/usr/bin/env python

from problem_1_4 import *

def test_replace_spaces_able():
    assert replace_spaces('ab le') == 'ab%20le'

def test_replace_spaces_backlog():
    assert replace_spaces('  ba ck log') == 'ba%20ck%20log'

def test_replace_spaces_carbonized():
    assert replace_spaces('ca rb on iz ed     ') == 'ca%20rb%20on%20iz%20ed'

def test_replace_spaces_documentarily():
    assert replace_spaces('    doc umentar ily     ') == 'doc%20umentar%20ily'

def test_replace_spaces_uncopyrightable():
    assert replace_spaces('  un  co   pyr ig ht ab le  ') == 'un%20%20co%20%20%20pyr%20ig%20ht%20ab%20le'

if __name__ == '__main__':
    test_replace_spaces_able()
    test_replace_spaces_backlog()
    test_replace_spaces_carbonized()
    test_replace_spaces_documentarily()
    test_replace_spaces_uncopyrightable()
