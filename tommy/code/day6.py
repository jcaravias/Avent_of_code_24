"""
There is a security guard that is facing the direction ^ is pointing
the guards actions
1. if blocked turn right
2. move step forward

how many distinct positions will the guard visit?

to solve:
1. Get the starting coordinates. 
2. Do DFS and keep a seen list to identify how many spots the guard has visited

an improvement on my algorithm would be to go the entire length of the guard's vision
and then only stop if I see a block or am out of bounds
"""
import copy

with open("tommy/txt_files/day6.txt") as f:
    grid = f.read().split('\n')
    grid = [list(i) for i in grid]

def valid_square(r,c):
    """returns if valid space for guard"""
    return (
        r >= 0 and 
        r < len(grid) and
        c >= 0 and
        c < len(grid[0])
    )
def get_starting_position(grid):
    """return starting position ^
    """
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                return (r,c)


def dfs1(r: int, c: int, dir: tuple, seen_coords: set):
    """
    Args:
        r (_type_): y coord
        c (_type_): x coord
        dir (_type_): the current direction we're heading in
    """
    if not valid_square(r,c): 
        return # outside the bounds of the grid 

    # if valid, add to seen
    seen_coords.add((r,c))
    # if the next possible square isn't valid, get out
    if not valid_square(r + dir[0], c + dir[1]):
        return 
    # if we see # in front of us turn right
    if grid[r + dir[0]][c + dir[1]] == '#':
        # how we turn right
        dir = (dir[1], -dir[0])
        dfs1(r,c,dir,seen_coords)
    # otherwise move 1 space forward in dir direction
    else: 
        dfs1(r + dir[0], c + dir[1], dir, seen_coords)

def dfs2(r: int, c: int, dir: tuple, seen_coords: set, copy_grid:list):
    """
    Args:
        r (_type_): y coord
        c (_type_): x coord
        dir (_type_): the current direction we're heading in
    """
    if not valid_square(r,c): 
        return 0 # outside the bounds of the grid 
    if (r,c, dir) in seen_coords:
        return 1

    # if valid, add to seen
    seen_coords.add((r,c, dir))
    # if the next possible square isn't valid, get out
    if not valid_square(r + dir[0], c + dir[1]):
        return 0
    # if we see # in front of us turn right
    if copy_grid[r + dir[0]][c + dir[1]] == '#':
        # how we turn right
        dir = (dir[1], -dir[0])
        return dfs2(r,c,dir,seen_coords, copy_grid)
    # otherwise move 1 space forward in dir direction
    else: 
        return dfs2(r + dir[0], c + dir[1], dir, seen_coords, copy_grid)
        

def main1():
    seen_coords = set()
    start_r, start_c = get_starting_position(grid)
    seen_coords.add((start_r, start_c))
    dfs1(start_r, start_c, (-1,0), seen_coords)
    return len(seen_coords)

def main2():
    """Lazy brute force solution where I go each point in the grid and 
    sub # to check if it creates a loop. A loop is created if I've already 
    seen a r,c,dir tuple

    Returns:
        _type_: _description_
    """
    rows, cols = len(grid), len(grid[0])
    seen_coords = set()
    start_r, start_c = get_starting_position(grid)
    ans = 0
    for r in range(rows):
        for c in range(cols):
            copy_grid = copy.deepcopy(grid)
            seen_coords = set()
            copy_grid[r][c] = '#'
            ans += dfs2(start_r, start_c, (-1,0), seen_coords, copy_grid)
    return ans


if __name__ == '__main__':
    import sys
    import time 
    sys.setrecursionlimit(10000) 
    st = time.time()
    print(f"Part 1 = {main1()}")
    et = time.time()
    print(f"Time for Part 1 = {et - st:,.5f} seconds")

    st = time.time()
    print(f"Part 2 = {main2()}")
    et = time.time()
    print(f"Time for Part 2 = {et - st:,.5f} seconds")
    
