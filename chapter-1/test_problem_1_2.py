#!/usr/bin/env python

from problem_1_2 import *

def test_reverse_able():
    assert reverse('able') == 'elba'

def test_reverse_backlog():
    assert reverse('backlog') == 'golkcab'

def test_reverse_carbonized():
    assert reverse('carbonized') == 'dezinobrac'

def test_reverse_documentarily():
    assert reverse('documentarily') == 'yliratnemucod'

def test_reverse_uncopyrightable():
    assert reverse('uncopyrightable') == 'elbathgirypocnu'

def test_reverse_ball():
    assert reverse('ball') == 'llab'

def test_reverse_pokemon():
    assert reverse('pokemon') == 'nomekop'

def test_reverse_abhorrence():
    assert reverse('abhorrence') == 'ecnerrohba'

def test_reverse_pianistically():
    assert reverse('pianistically') == 'yllacitsinaip'

def test_reverse_pyroelectricities():
    assert reverse('pyroelectricities') == 'seiticirtceleoryp'

if __name__ == '__main__':
    test_reverse_able()
    test_reverse_backlog()
    test_reverse_carbonized()
    test_reverse_documentarily()
    test_reverse_uncopyrightable()
    test_reverse_ball()
    test_reverse_pokemon()
    test_reverse_abhorrence()
    test_reverse_pianistically()
    test_reverse_pyroelectricities()