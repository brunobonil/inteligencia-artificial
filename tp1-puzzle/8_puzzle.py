from random import randint
from copy import deepcopy

puzzle = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 'X']]

def finder(): # Devuelve lista con la posición de 'X' Ej: [2, 2]
    for i in puzzle:
        if 'X' in i:
            return [puzzle.index(i), i.index('X')]

def moves(dir, fila, col):
    
    if dir == 1: #IZQUIERDA
        puzzle[fila][col], puzzle[fila][col-1] = puzzle[fila][col-1], puzzle[fila][col]
    if dir == 2: #DERECHA
        puzzle[fila][col], puzzle[fila][col+1] = puzzle[fila][col+1], puzzle[fila][col]
    if dir == 3: #ARRIBA
        puzzle[fila][col], puzzle[fila-1][col] = puzzle[fila-1][col], puzzle[fila][col]
    if dir == 4: #ABAJO
        puzzle[fila][col], puzzle[fila+1][col] = puzzle[fila+1][col], puzzle[fila][col]

def possible_moves():
    fila = finder()[0]
    col = finder()[1]
    pos_moves = [] 
    if col != 0:
        pos_moves.append(1)
    if col != 2:
        pos_moves.append(2)
    if fila != 0:
        pos_moves.append(3)
    if fila != 2:
        pos_moves.append(4)
    return [pos_moves, [fila, col]]

def mix():
    for i in range(20):
        poss_moves = possible_moves()[0]
        fila = possible_moves()[1][0]
        col = possible_moves()[1][1]
        ran_move = randint(0, len(poss_moves)-1)
        dir = poss_moves[ran_move]
        moves(dir, fila, col)

def solución_random():
    counter = 0
    while puzzle != [[1,2, 3], [4, 5, 6], [7, 8, 'X']]:
        mix()
        counter += 1
    return counter

def solución_anchura():
    inicial = puzzle
    

mix()
for i in puzzle:
    print(i)
print('\n')


#print(f"Número de movimientos: {solución_random()}")


