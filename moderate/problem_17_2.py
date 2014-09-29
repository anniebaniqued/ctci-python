#!/usr/bin/env python

# Problem Statement:
# Design an algorithm to figure out if someone has won a game of tic-tac-toe
#
# Let's assume that game states are represented as below:
# 0 -> empty
# 1 -> cross (X)
# 2 -> circle (O)

def has_won_3x3(board):
    # Here is a 3x3 board matrix
    # [ [i, i, i]
    #   [j, j, j]
    #   [k, k, k]]
    empty = 0
    cross = 1
    circle = 2

    for x in range(0, 3):
        # Check Rows
        if board[x][0] != empty:
            if board[x][0] == board[x][1] and \
               board[x][0] == board[x][2]:
                return board[x][0] # return the piece that won

        # Check Columns
        if board[0][x] != empty:
            if board[0][x] == board[1][x] and \
               board[0][x] == board[2][x]:
                return board[0][x] # return the piece that won

    # Check Diagonal
    if board[0][0] != empty:
        if board[0][0] == board[1][1] and \
           board[0][0] == board[2][2]:
            return board[0][0] # return the piece that won

    # Check Reverse Diagonal
    if board[0][2] != empty:
        if board[0][2] == board[1][1] and \
           board[0][2] == board[2][0]:
            return board[0][2] # return the piece that won

    return empty # nobody won

def has_won_NxN(board, n):
    # Here is a NxN board matrix
    # [ [i, i, i, ...]
    #   [j, j, j, ...]
    #   [k, k, k, ...]
    #   [.  .  .  ...]
    #   [.  .  .  ...]]
    empty = 0
    cross = 1
    circle = 2

    # Check Rows
    for row in range(0, n):
        if board[row][0] != empty:
            for col in range (1, n):
                if board[row][col] != board[row][col-1]:
                    break
            if col == n-1:
                return board[row][0]

    # Check Rows
    for col in range(0, n):
        if board[0][col] != empty:
            for row in range (1, n):
                if board[row][col] != board[row-1][col]:
                    break
            if row == n-1:
                return board[0][col]

    # Check Diagonal
    if board[0][0] != empty:
        for x in range(1, n):
            if board[x][x] != board[x-1][x-1]:
                break
        if x == n-1:
            return board[0][0]

    # Check Reverse Diagonal
    if board[n-1][0] != empty:
        for x in range(1, n):
            if board[n-1-x][x] != board[n-x][x-1]:
                break
        if x == n-1:
            return board[n-1][0]

    return empty

