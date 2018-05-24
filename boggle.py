from string import ascii_uppercase
from random import choice

def make_grid(cols, rows):
    return{(c, r): choice(ascii_uppercase)
                    for c in range(cols)
                    for r in range(rows)
    }


# def make_grid(cols, rows):
#     grid = {}
#     for c in range(cols): #if cols is 5 c will be 0 to 4
#         for r in range(rows): # if rows is 3 r will be 0 to 2
#             grid[(c, r)] = choice(ascii_uppercase)
#     return grid
    
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

def all_grid_neighbours(grid):
  return {pos: [n for n in get_neighbours(pos) if n in grid] for pos in grid}
            
# def all_grid_neighbours(grid):
#     neighbours_of = {}
#     for pos in grid:
#         neighbours = get_neighbours(pos)
        
#         real_neighbours = []
#         for n in neighbours:
#             if n in grid:
#                 real_neighbours.append(n)
#         neighbours_of[pos] = real_neighbours
#     return neighbours_of
        
def path_to_word(grid, path):
    word = ""
    for pos in path:
        word = word + grid[pos] #(word += grid[pos])
    return word
#[k  for  k in  path.keys()]

def read_wordfile(filename):
    f = open(filename, "r")
    text = f.read().upper()
    words = text.split("\n") 
    f.close()
    return set(words)
    
#print(read_wordfile("bogwords.txt"))

# def read_wordfile(filename):
#     f = open(filename, "r")
#     text = f.read().upper()
#     words = text.splitlines()
#     f.close()
#     return words
    

# def read_wordfile(filename):
#     f = open(filename, "r")
#     words = f.read().splitlines()
#     words = [ word.upper() for word in words]
#     f.close()
#     return words

def search(grid, wordlist):
    all_neighbours = all_grid_neighbours(grid)

    def do_search(path, positions):
        # If no more positions to search, there won't be any more words    
        if positions == []:
            return []
        
        # Extend the path by the first position and check if it's a word    
        this_position = positions[0]
        this_path = path + [this_position]
        this_word = path_to_word(grid, this_path)
        # Either it was a word, or it wasn't
        if this_word in wordlist:
            words = [this_word]
        else:
            words = []

        # Find which neighbours of the current position, have not been used
        # Search on extending the current path by the neighbours
        neighbours = [n for n in all_neighbours[this_position] if n not in path]
        words += do_search(this_path, neighbours)
        
        # Search on from the last path, using the siblings of the current position
        words += do_search(path, positions[1:])
        
        # Return all the words found on this branch
        return words
            
    return do_search([], list(grid.keys()))   



def display(words):
    for word in words:
        print(word)
    print("Found %s words" % len(words))

def main():
    grid = make_grid(4, 4)
    dictionary = read_wordfile("bogwords.txt")
    words = set(search(grid, dictionary))
    display(words)

if __name__ == "__main__": 
    main()



