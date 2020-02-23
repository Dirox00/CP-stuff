def neighbours(node, grid):
    '''Dada la posición(x, y) en una array "grid"
       devuelve los vecinos(incluidas diagonales) 
       en forma de posición(x, y)
    '''
    length, width = len(grid), len(grid[0])
    x, y = node
    for j in range(max(y - 1, 0), min(y + 1, length - 1) + 1):
        for i in range(max(x - 1, 0), min(x + 1, width - 1) + 1):
            if (x, y) == (i, j):
                continue
            yield i, j

def locate(x, matrix):
    for j, row in enumerate(matrix):
        for i, element in enumerate(row):
            if element == x:
                return i, j

def print_matrix(matrix):
    for row in matrix:
        print(''.join(str(x) for x in row))
