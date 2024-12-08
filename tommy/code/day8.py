with open("tommy/txt_files/day8.txt") as file:
    grid = file.read().split('\n')
    grid = [list(i) for i in grid]

# get coordinates of all unique symbols
def get_symbols(grid: list) -> dict[list]:
    """for all unique symbols in the grid, map to their coords
    Args:
        grid (list): board where the symbols are kept
    Returns:
        dict: symbol: [coords]
    """
    symbol_map = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.':
                continue
            symbol = grid[r][c]
            symbol_map[symbol] = symbol_map.get(symbol,[]) + [(r,c)]

    return symbol_map

def valid_coord(coord):
    if coord is None:
        return False
    
    r,c = coord
    return (
        r >= 0 and
        r < len(grid) and
        c >= 0
        and c < len(grid[0])
    )
def valid_coord_list(coord_list):
    return {coord for coord in coord_list if valid_coord(coord)}

def get_resonance_coords(coord1: tuple, coord2: tuple):
    """Given two coords, get the resulting resonance coords they produce
    Args:
        coord1 (tuple): 
        coord2 (tuple): 
    """
    r1,c1 = coord1
    r2,c2 = coord2

    resonance1 = (r2 + (r2 - r1), c2 + (c2 - c1))
    resonance2 = (r1 + (r1 - r2), c1 + (c1 - c2))

    if not valid_coord(resonance1):
        resonance1 = None
    if not valid_coord(resonance2):
        resonance2 = None

    return {resonance1, resonance2}

def get_all_resonance_coords(coord1: tuple, coord2: tuple):
    r1,c1 = coord1
    r2,c2 = coord2
    dr,dc = (r2 - r1), (c2 - c1)
    resonance_list = {(r1,c1), (r2,c2)}
    for i in range(-50,50):
        new_coord = r1 + i*dr, c1 + i*dc
        if not valid_coord(new_coord):
            continue
        resonance_list.add(new_coord)
    return resonance_list


def check_all_pairings(coords_list, all_coords=False):
    """
    For a coord list return the set of valid coords that are created from 
    get resonance_coords
    """
    antinode_loc = set()
    for i in range(len(coords_list) - 1):
        for j in range(i+1, len(coords_list)):
            coord1 = coords_list[i]
            coord2 = coords_list[j]
            if all_coords:
                resonance_list = get_all_resonance_coords(coord1, coord2)
            else:
                resonance_list = get_resonance_coords(coord1, coord2)
            resonance_list = valid_coord_list(resonance_list)
            antinode_loc = antinode_loc.union(resonance_list)
      
    return antinode_loc


# for each symbol type, get the location of where the resonance symbols should be
def main1():
    symbol_map = get_symbols(grid)
    # print(symbol_map)
    antinode_loc = set()
    # for each symbol get valid locations
    for symbol, coords_list in symbol_map.items():
        antinode_loc = antinode_loc.union(check_all_pairings(coords_list))
    return len(antinode_loc)

def main2():
    symbol_map = get_symbols(grid)
    # print(symbol_map)
    antinode_loc = set()
    # for each symbol get valid locations
    for symbol, coords_list in symbol_map.items():
        antinode_loc = antinode_loc.union(check_all_pairings(coords_list, all_coords=True))
    return len(antinode_loc)


if __name__ == '__main__':

    print(f'Part 1 = {main1()}')
    print(f"Part 2 = {main2()}")