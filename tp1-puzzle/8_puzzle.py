from random import randint

puzzle = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 'X']]

def finder(): # Devuelve lista con la posición de 'X' Ej: [2, 2]
    for i in puzzle:
        if 'X' in i:
            return [puzzle.index(i), i.index('X')] 

def left():
    fila = finder()[0]
    col = finder()[1]
    if col != 0:
        puzzle[fila][col], puzzle[fila][col-1] = puzzle[fila][col-1], puzzle[fila][col]

def right():
    fila = finder()[0]
    col = finder()[1]
    if col != 2:
        puzzle[fila][col], puzzle[fila][col+1] = puzzle[fila][col+1], puzzle[fila][col]

def up():
    fila = finder()[0]
    col = finder()[1]
    if fila != 0:
        puzzle[fila][col], puzzle[fila-1][col] = puzzle[fila-1][col], puzzle[fila][col]

def down():
    fila = finder()[0]
    col = finder()[1]
    if fila != 2:
        puzzle[fila][col], puzzle[fila+1][col] = puzzle[fila+1][col], puzzle[fila][col]

def mix():
    for i in range(20):
        move = randint(1, 4)
        if move == 1:
            left()
        if move == 2:
            right()
        if move == 3:
            up()
        if move == 4:
            down()

def random():
    counter = 0
    while puzzle != [[1,2, 3], [4, 5, 6], [7, 8, 'X']]:
        mix()
        counter += 1
    return counter

mix()
for i in puzzle:
    print(i)
print('\n')

print(f"Número de movimientos: {random()}")

for i in puzzle:
    print(i)
print('\n')

