from random import randint
from copy import deepcopy


class Nodo:
    def __init__(self):
        self.padre = None
        self.hijos = []
        self.tabla = None


        
puzzle = [[1, 2, 3], 
         ['X', 5, 6], 
         [4, 7, 8]]
#puzzle = [['X', 2, 3], [1, 8, 5], [4, 7, 6]]

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
        poss_moves = possible_moves(board) # Retorna lista con posibles mov y posición
        fila, col = finder(board)
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
    nivel_act = [board]
    lvl_counter = 0
    while True:
        nivel_prox = []
        lvl_counter += 1
        for x in nivel_act: # Cambiar lista de tableros por lista de nodos
            pos_moves = possible_moves(x)
            fila, col = finder(x)
            padre = Nodo()
            padre.tabla = x
            for i in pos_moves:
                n = Nodo()
                n.tabla = deepcopy(x)
                n.padre = padre
                padre.hijos.append(n)
                moves(n.tabla, i, fila, col)
                if n.tabla == [[1, 2, 3], [4, 5, 6], [7, 8, 'X']]:
                    return (f"La solución se encontró en el nivel {lvl_counter}")
                #if n.tabla == 
                nivel_prox.append(n.tabla)
            nivel_act = nivel_prox
        print(len(nivel_act))

        

    

    

#mix()
for i in puzzle:
    print(i)
print('\n')


print(solución_anchura(puzzle))

#print(f"Número de movimientos: {solución_random()}")

# for i in puzzle:
#     print(i)
# print('\n')




