#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PROJECT: pikman
CREATED: Tue Apr  7 20:02:08 2020
AUTHOR(S): Haley Kruger & Chris Kruger
LICENSE: This is open-source software released under the terms of the
GPL (http://www.gnu.org/licenses/gpl.html).
OVERVIEW: Project used to learn python graphics library for a fun twist on a classic game.
-----------------------------------------------------------
"""

from graphics import *
# Used John Zelle's graphics lib from https://mcsp.wartburg.edu/zelle/python/graphics.py
import time


def draw_rec(board_column, board_row, color, dot_size):
    rtl = (board_column * (size * 2)) + offsetC
    rtr = (board_row * (size * 2)) + offsetR
    rbl = (board_column * (size * 2) + offsetC + (dot_size * 2))
    rbr = (board_row * (size * 2) + offsetR + (dot_size * 2))

    head = Rectangle(Point(rtl, rtr), Point(rbl, rbr))

    head.setFill(color)
    head.setOutline(color)
    head.draw(win)


def draw_circle(board_column, board_row, color, dot_size):
    if color != "white":
        head = Circle(Point((board_column * (size * 2) +
                             (offsetC + dot_size)), (board_row * (size * 2) + (offsetR + dot_size))), dot_size)
        head.setFill(color)
    else:
        head = Circle(Point((board_column * (size * 2) + (offsetC + dot_size)),
                            (board_row * (size * 2) + (offsetR + dot_size))), dot_size / 3)
        head.setFill(color)
    head.draw(win)


def draw_board(current_board):
    print("Game On")
    for boardRow in range(gameBoardSize[0]):
        for boardColumn in range(gameBoardSize[1]):
            check_color = gameColor[gameBoard[boardRow][boardColumn]]
            if check_color == "blue":
               draw_rec(boardColumn, boardRow, gameColor[gameBoard[boardRow][boardColumn]], size)
            else:
               draw_circle(boardColumn, boardRow, gameColor[gameBoard[boardRow][boardColumn]], size)


def erase_board(current_board):
    print("Game Over")
    for boardRow in range(gameBoardSize[0]):
        for boardColumn in range(gameBoardSize[1]):
            draw_rec(boardColumn, boardRow, gameColor[0], size)
        print(' ')


def animate_board():
    #    print("animateBoard")
    for boardRow in range(gameBoardSize[0]):
        for boardColumn in range(gameBoardSize[1]):
            if gameBoard[boardRow][boardColumn] == 3:
                draw_circle(boardColumn, boardRow, gameColor[gameBoard[boardRow][boardColumn]], size)
                gameBoard[boardRow][boardColumn] = 4
            elif gameBoard[boardRow][boardColumn] == 4:
                draw_circle(boardColumn, boardRow, gameColor[gameBoard[boardRow][boardColumn]], size)
                gameBoard[boardRow][boardColumn] = 3


def debug_print():
    print("movepikman: C:" + str(pikLocation[0]) + " R:" + str(pikLocation[1]))
    print(" " + str(gameBoard[pikLocation[0] + 1][pikLocation[1] - 1]) + str(
        gameBoard[pikLocation[0] + 1][pikLocation[1] + 0]) + str(gameBoard[pikLocation[0] + 1][pikLocation[1] + 1]))
    print(" " + str(gameBoard[pikLocation[0] - 0][pikLocation[1] - 1]) + "x" + str(
        gameBoard[pikLocation[0] + 0][pikLocation[1] + 1]))
    print(" " + str(gameBoard[pikLocation[0] - 1][pikLocation[1] - 1]) + str(
        gameBoard[pikLocation[0] - 1][pikLocation[1] - 0]) + str(gameBoard[pikLocation[0] - 1][pikLocation[1] + 1]))


def draw_pik_score(pik_score, game_timer):
    scoreText.setText("Score: " + str(pik_score) + " Timer: " + str(game_timer))


def draw_notice(note_message, note_color):
    noticeText.setText(note_message)
    noticeText.setTextColor(note_color)


def draw_pikman(pik_location, pik_color1):
    if pik_color1 == "yellow":
        pik_color1 = "orange"
        draw_circle(pik_location[1], pik_location[0], pik_color1, size)
    else:
        pik_color1 = "yellow"
        draw_circle(pik_location[1], pik_location[0], pik_color1, size)
#        head = Circle(Point((board_column * (size * 2) + (offsetC + dot_size)), (board_row * (size * 2) + (offsetR + dot_size))), dot_size)
        head1 = Polygon(Point((pik_location[1] * (size * 2) + (offsetC + size)), (pik_location[0] * (size * 2) + (offsetR+size))),
                        Point((pik_location[1] * (size * 2) + offsetC + size*2),
                              (pik_location[0] * (size * 2) + offsetR + size*2)),
                        Point((pik_location[1] * (size * 2) + offsetC + size*2),
                              (pik_location[0] * (size * 2) + (offsetR + size)))
                        )
        head1.setFill("black")
        head1.draw(win)
    return pik_color1


def check_score(pik_row, pik_col):
    global pikScore
    if gameBoard[pik_row][pik_col] == 3:
        draw_pik_score(pikScore, "black")
        pikScore = pikScore + 100
        draw_pik_score(pikScore, "white")
        gameBoard[pik_row][pik_col] = 0
    if gameBoard[pik_row][pik_col] == 4:
        draw_pik_score(pikScore, "black")
        pikScore = pikScore + 100
        draw_pik_score(pikScore, "white")
        gameBoard[pik_row][pik_col] = 0
    if gameBoard[pik_row][pik_col] == 5:
        draw_pik_score(pikScore, "black")
        pikScore = pikScore + 10
        draw_pik_score(pikScore, "white")
        gameBoard[pik_row][pik_col] = 0


def move_pikman(pik_move):
    #    print("movepikman:" + str(pikLocation[0]) + str(pikLocation[1]))
    draw_circle(pikLocation[1], pikLocation[0], gameColor[0], size)
    global pikScore

    if pik_move == 'X' or pik_move == 'x':  # Down
        print("check " + str(gameBoard[pikLocation[0] - 1][pikLocation[1] - 0]))
        check_score((pikLocation[0] - 1),(pikLocation[1] - 0))
        if gameBoard[pikLocation[0] - 1][pikLocation[1] - 0] != 1:
            pikLocation[0] = pikLocation[0] - 1
            pikLocation[1] = pikLocation[1] - 0
    elif pik_move == 'D' or pik_move == 'd':  # Right
        print("check " + str(gameBoard[pikLocation[0] + 0][pikLocation[1] + 1]))
        check_score((pikLocation[0] + 0),(pikLocation[1] + 1))
        if gameBoard[pikLocation[0] + 0][pikLocation[1] + 1] != 1:
            pikLocation[0] = pikLocation[0] + 0
            pikLocation[1] = pikLocation[1] + 1
    elif pik_move == 'W' or pik_move == 'w':  # Up
        print("check " + str(gameBoard[pikLocation[0] + 1][pikLocation[1] + 0]))
        check_score((pikLocation[0] + 1),(pikLocation[1] + 0))
        if gameBoard[pikLocation[0] + 1][pikLocation[1] + 0] != 1:
            pikLocation[0] = pikLocation[0] + 1
            pikLocation[1] = pikLocation[1] + 0
    elif pik_move == 'A' or pik_move == 'a':  # Left
        print("check " + str(gameBoard[pikLocation[0] - 0][pikLocation[1] - 1]))
        check_score((pikLocation[0] - 0),(pikLocation[1] - 1))
        if gameBoard[pikLocation[0] - 0][pikLocation[1] - 1] != 1:
            pikLocation[0] = pikLocation[0] - 0
            pikLocation[1] = pikLocation[1] - 1
    debug_print()
    print("movepikman: C:" + str(pikLocation[0]) + " R:" + str(pikLocation[1]) + " K:" + str(pik_move))


def check_capture():
    print("checkCapture")


def calc_score():
    print("calcScore")


def final_score():
    print("finalScore")


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

game1 = (
    [1, 1, 1, 1, 1, 1, 1],
    [1, 3, 5, 5, 5, 3, 1],
    [1, 5, 1, 1, 1, 5, 1],
    [1, 5, 5, 1, 5, 5, 1],
    [1, 1, 5, 5, 5, 1, 1],
    [1, 5, 5, 1, 5, 5, 1],
    [1, 5, 1, 4, 1, 5, 1],
    [1, 5, 1, 5, 1, 5, 1],
    [1, 5, 1, 5, 1, 5, 1],
    [1, 5, 5, 5, 5, 5, 1],
    [1, 1, 1, 1, 1, 1, 1])

game2 = (
    [1, 1, 1, 1, 1, 1, 1],
    [1, 5, 5, 5, 5, 3, 1],
    [1, 5, 1, 1, 1, 5, 1],
    [1, 5, 5, 1, 5, 5, 1],
    [1, 1, 5, 5, 5, 1, 1],
    [1, 5, 5, 5, 5, 5, 1],
    [1, 5, 1, 5, 1, 5, 1],
    [1, 5, 1, 5, 1, 5, 1],
    [1, 5, 1, 5, 1, 5, 1],
    [1, 4, 5, 1, 5, 4, 1],
    [1, 1, 1, 1, 1, 1, 1])

gameBoard = game2
gameBoardSize = [11,7]
gameColor = ["black", "blue", "red", "pink", "green", "white"]
pikLocation = [4, 3]  # R, C (goofy)
pikColor = 2
pikScore = 0
maxScore = 590

size = 20 # 10 is the minimum for now
offsetC = size * 4
offsetR = size * 2
win = GraphWin("pikMan", (size * 20), (size * 30))
win.setCoords(size, size, (size * 20), (size * 30))

gameStart = time.time()
gameTimer = 0.0
gameDuration = 25
alive = True

print('hello, pikman')
print(gameBoard[1][2])

win.setBackground("black")
#win.setBackground("white")
draw_board(gameBoard)

noticeText = Text(Point(win.getWidth() / 2, 250), "Welcome to Wonderland")
noticeText.setTextColor("yellow")
noticeText.draw(win)
scoreText = Text(Point(win.getWidth() / 2, 270), "127.0.0.1")
scoreText.setTextColor("white")
scoreText.draw(win)

pikColor = draw_pikman(pikLocation, pikColor)
draw_notice("Click anywhere to quit", "yellow")
draw_pik_score(pikScore, "0")
debug_print()

# ---------------------------------------------------------
# Start game loop
# ---------------------------------------------------------
while alive:
    #    if checkCapture():
    #        alive = False
    #    else:
    #        calcScore()
    coordinate = win.checkMouse()
    if coordinate is not None:
        alive = False

    move = win.checkKey()
    if move != "":
        move_pikman(move)

    if (gameDuration - gameTimer) < 0:
        alive = False
    else:
        # gameTimer = gameTimer - 1
        gameTimer = time.time() - gameStart
        draw_pik_score(pikScore, f"{gameTimer:.1f}")
        print("time: " + str(f'{gameTimer:.1f}'))
    animate_board()
    pikColor = draw_pikman(pikLocation, pikColor)
    if pikScore >= maxScore:
        draw_notice("Click anywhere to quit", "black")
        draw_notice("Winner!", "yellow")
        alive = False

    time.sleep(.1)

erase_board(gameBoard)
win.getMouse()
final_score()
win.close()
print("the end")