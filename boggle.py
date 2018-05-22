from string import ascii_uppercase
from random import choice

def make_grid(cols, rows):
    grid = {}
    for c in range(cols): #if cols is 5 c will be 0 to 4
        for r in range(rows): # if rows is 3 r will be 0 to 2
            grid[(c, r)] = choice(ascii_uppercase)
    return grid
    
    # {
    #     (0, 0): "?",
    #     (1, 0): "?",
    #     (0, 1): "?",
    #     (1, 1): "?",
        
    # }
def get_neighbours(pos):
    col, row = pos
    return [
            (col-1, row-1), 
            (col, row-1),
            (col+1, row-1),
            (col+1, row),
            (col+1, row+1),
            (col, row+1),
            (col-1,row+1),
            (col-1,row),
            ]
