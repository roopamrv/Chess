import pygame
import time
import sys

board = [[' ' for i in range(8)] for i in range(8)]


class Piece:

    def __init__(self, team, types, image, killable=False):
        self.team = team
        self.types = types
        self.image = image
        self.killable = killable


bpawn = Piece('b', 'pawn', 'images/black_pawn.png')
wpawn = Piece('w', 'pawn', 'images/white_pawn.png')
bknight = Piece('b', 'knight', 'images/black_knight.png')
wknight = Piece('w', 'knight', 'images/white_knight.png')
bking = Piece('b', 'king', 'images/black_king.png')
wking = Piece('w', 'king', 'images/white_king.png')
bqueen = Piece('b', 'queen', 'images/black_queen.png')
wqueen = Piece('w', 'queen', 'images/white_queen.png')
brook = Piece('b', 'rook', 'images/black_rook.png')
wrook = Piece('w', 'rook', 'images/white_rook.png')
bbishop = Piece('b', 'bishop', 'images/black_bishop.png')
wbishop = Piece('w', 'bishop', 'images/white_bishop.png')

start_order = {
    (0, 0): pygame.image.load(brook.image),
    (1, 0): pygame.image.load(bknight.image),
    (2, 0): pygame.image.load(bbishop.image),
    (3, 0): pygame.image.load(bking.image),
    (4, 0): pygame.image.load(bqueen.image),
    (5, 0): pygame.image.load(bbishop.image),
    (6, 0): pygame.image.load(bknight.image),
    (7, 0): pygame.image.load(brook.image),
    (0, 1): pygame.image.load(bpawn.image),
    (1, 1): pygame.image.load(bpawn.image),
    (2, 1): pygame.image.load(bpawn.image),
    (3, 1): pygame.image.load(bpawn.image),
    (4, 1): pygame.image.load(bpawn.image),
    (5, 1): pygame.image.load(bpawn.image),
    (6, 1): pygame.image.load(bpawn.image),
    (7, 1): pygame.image.load(bpawn.image),
    (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None, (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None,
    (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None, (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None,
    (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None, (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None,
    (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None, (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None,
    (0, 6): pygame.image.load(wpawn.image),
    (1, 6): pygame.image.load(wpawn.image),
    (2, 6): pygame.image.load(wpawn.image),
    (3, 6): pygame.image.load(wpawn.image),
    (4, 6): pygame.image.load(wpawn.image),
    (5, 6): pygame.image.load(wpawn.image),
    (6, 6): pygame.image.load(wpawn.image),
    (7, 6): pygame.image.load(wpawn.image),
    (0, 7): pygame.image.load(wrook.image),
    (1, 7): pygame.image.load(wknight.image),
    (2, 7): pygame.image.load(wbishop.image),
    (3, 7): pygame.image.load(wking.image),
    (4, 7): pygame.image.load(wqueen.image),
    (5, 7): pygame.image.load(wbishop.image),
    (6, 7): pygame.image.load(wknight.image),
    (7, 7): pygame.image.load(wrook.image),
}


def create_board(board):
    board[0] = [Piece('b', 'rook', 'images/black_rook.png'), Piece('b', 'knight', 'images/black_knight.png'),
                Piece('b', 'bishop', 'images/black_bishop.png'),
                Piece('b', 'queen', 'images/black_queen.png'), Piece('b', 'king', 'images/black_king.png'),
                Piece('b', 'bishop', 'images/black_bishop.png'), Piece('b', 'knight', 'images/black_knight.png'),
                Piece('b', 'rook', 'images/black_rook.png')]

    board[7] = [Piece('w', 'rook', 'images/white_rook.png'), Piece('w', 'knight', 'images/white_knight.png'),
                Piece('w', 'bishop', 'images/white_bishop.png'),
                Piece('w', 'queen', 'images/white_queen.png'), Piece('w', 'king', 'images/white_king.png'),
                Piece('w', 'bishop', 'images/white_bishop.png'), Piece('w', 'knight', 'images/white_knight.png'),
                Piece('w', 'rook', 'images/white_rook.png')]

    for i in range(0, 8):
        board[1][i] = Piece('b', 'pawn', 'images/black_pawn.png')
        board[6][i] = Piece('w', 'pawn', 'images/white_pawn.png')

    return board


# Function to check whether the movement is within the game_board or not
def check_move(pos):
    if -1 < pos[0] < 8 and -1 < pos[1] < 8:
        return True


# grid in readable manner
def readable_manner(board):
    op = ''

    for i in board:
        for j in i:
            try:
                op += j.team + j.type + ','
            except:
                op += j + ','
        op += '\n'
    return op


# deselecting grid to remove highlighted box and killable pieces
def deselect():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'x ':
                board[i][j] = ' '
            else:
                try:
                    board[i][j].killable = False
                except:
                    pass

    return readable_manner(board)


# highlights of valid moves
def highlight(board):
    highlighted = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'x ':
                highlighted.append((i, j))
            else:
                try:
                    if board[i][j].killable:
                        highlighted.append((i, j))
                except:
                    pass
    return highlighted


# Team
def team(moves, index):
    row, column = index
    if moves % 2 == 0:
        if board[row][column] == 'w':
            return True
    else:
        if board[row][column] == 'b':
            return True

# movement
