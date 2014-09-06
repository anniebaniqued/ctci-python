#!/usr/bin/env python

from problem_1_3 import *

def test_check_if_permutation_able_elba():
    assert check_if_permutation('able', 'elba') == True

def test_check_if_permutation_backlog_golkcab():
    assert check_if_permutation('backlog', 'golkcab') == True

def test_check_if_permutation_carbonized_dezinobrac():
    assert check_if_permutation('carbonized', 'dezinobrac') == True

def test_check_if_permutation_documentarily_yliratnemucod():
    assert check_if_permutation('documentarily', 'yliratnemucod') == True

def test_check_if_permutation_uncopyrightable_elbathgirypocnu():
    assert check_if_permutation('uncopyrightable', 'elbathgirypocnu') == True

def test_check_if_permutation_ball_laab():
    assert check_if_permutation('ball', 'laab') == False

def test_check_if_permutation_pokemon_namekop():
    assert check_if_permutation('pokemon', 'namekop') == False

def test_check_if_permutation_abhorrence_ecnerrohbe():
    assert check_if_permutation('abhorrence', 'ecnerrohbe') == False

def test_check_if_permutation_pianistically_yllacitsinaid():
    assert check_if_permutation('pianistically', 'yllacitsinaid') == False

def test_check_if_permutation_pyroelectricities_seiticirtceleorip():
    assert check_if_permutation('pyroelectricities', 'seiticirtceleorip') == False

if __name__ == '__main__':
    test_check_if_permutation_able_elba()
    test_check_if_permutation_backlog_golkcab()
    test_check_if_permutation_carbonized_dezinobrac()
    test_check_if_permutation_documentarily_yliratnemucod()
    test_check_if_permutation_uncopyrightable_elbathgirypocnu()
    test_check_if_permutation_ball_laab()
    test_check_if_permutation_pokemon_namekop()
    test_check_if_permutation_abhorrence_ecnerrohbe()
    test_check_if_permutation_pianistically_yllacitsinaid()
    test_check_if_permutation_pyroelectricities_seiticirtceleorip()
