from lib2to3.pytree import Node
from random import randint
from copy import deepcopy


class Nodo:
    def __init__(self):
        self.padre = None
        self.hijos = []
        self.tabla = None

    def agregar_hijos(self, nodo):
        self.tabla.append(nodo)

    
        
# puzzle = [[1, 2, 3], 
#           [4, 5, 6], 
#           [7, 8, 'X']]
puzzle = [['X', 2, 3], [1, 8, 5], [4, 7, 6]]

def finder(board): # Devuelve lista con la posición de 'X' Ej: [2, 2]
    for i in board:
        if 'X' in i:
            return [board.index(i), i.index('X')]

def moves(board, dir, fila, col):
    
    if dir == 1: #IZQUIERDA
        board[fila][col], board[fila][col-1] = board[fila][col-1], board[fila][col]
    if dir == 2: #DERECHA
        board[fila][col], board[fila][col+1] = board[fila][col+1], board[fila][col]
    if dir == 3: #ARRIBA
        board[fila][col], board[fila-1][col] = board[fila-1][col], board[fila][col]
    if dir == 4: #ABAJO
        board[fila][col], board[fila+1][col] = board[fila+1][col], board[fila][col]

def possible_moves(board):
    fila, col = finder(board) 
    pos_moves = [] 
    if col != 0:
        pos_moves.append(1)
    if col != 2:
        pos_moves.append(2)
    if fila != 0:
        pos_moves.append(3)
    if fila != 2:
        pos_moves.append(4)
    return pos_moves

def mix(board):
    for i in range(20):
        poss_moves = possible_moves()[0] # Retorna lista con posibles mov y posición
        fila = possible_moves()[1][0]
        col = possible_moves()[1][1]
        ran_move = randint(0, len(poss_moves)-1)
        dir = poss_moves[ran_move]
        moves(board, dir, fila, col)

def solución_random(board):
    counter = 0
    while puzzle != [[1,2, 3], [4, 5, 6], [7, 8, 'X']]:
        mix(board)
        counter += 1
    return counter

def solución_anchura(board):     # puzzle = [['X', 2, 3], [1, 8, 5], [4, 7, 6]]
    poss_moves = possible_moves()[0]
    fila = possible_moves()[1]
    col = possible_moves()[2]
    padre = Nodo()
    padre.tabla = board
    

    

#mix()
for i in puzzle:
    print(i)
print('\n')


solución_anchura(puzzle)

#print(f"Número de movimientos: {solución_random()}")

# for i in puzzle:
#     print(i)
# print('\n')




