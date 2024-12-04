with open('tommy/txt_files/day4.txt') as f:
    data = f.read().split('\n')
    data = [[i for i in line] for line in data]


def continue_word(word):
    """check if word is on the right path
    """
    if len(word) == 0:
        return True
    if len(word) == 1:
        return word == 'X'
    if len(word) == 2:
        return word == 'XM'
    if len(word) == 3:
        return word == 'XMA'
    if len(word) == 4:
        return word == 'XMAS'

def dfs(c, r, current_word, dir):
    """
    use dfs to traverse the graph and find all instances of xmas

    dir is the current direction we're traveling
    """
    
    if (
        c >= len(data) or
        r >= len(data[0]) or
        r < 0 or 
        c < 0 or
        data[c][r] not in 'XMAS' or
        not continue_word(current_word + data[c][r])
    ):
        return 0
    
    current_word += data[c][r]
    if current_word == 'XMAS':
        return 1
    # we haven't established a direction
    if dir is None:
        return (
            dfs(c+1,r, current_word, (1,0)) + 
            dfs(c-1,r, current_word, (-1,0)) +
            dfs(c,r+1, current_word, (0,1)) +
            dfs(c,r-1, current_word, (0,-1)) +
            dfs(c-1,r-1, current_word, (-1,-1)) +
            dfs(c+1,r+1, current_word, (1,1)) +
            dfs(c-1,r+1, current_word, (-1,1)) +
            dfs(c+1,r-1, current_word, (1,-1)) 
            )
    # otherwise continue in direction we're already going 
    return dfs(c+dir[0], r+dir[1], current_word, dir) 
    
def main1():
    ans = 0
    cols, rows = len(data), len(data[0])
    for c in range(cols):
        for r in range(rows):
            if data[c][r] != 'X':
                continue

            ans += dfs(c,r,'', None)
    return ans


def not_valid_coord(c,r):
    return (
        c >= len(data) or
        r >= len(data[0]) or
        r < 0 or 
        c < 0 or
        data[c][r] not in 'MAS'
    )


def check_match(coord1, coord2):
    """checks if two data points are the same value
    """
    c1,r1 = coord1
    c2,r2 = coord2
    # if either coord in not valid, return False
    if not_valid_coord(c1,r1) or not_valid_coord(c2,r2):
        return 0

    if data[c1][r1] == data[c2][r2]:
        return data[c1][r1]
    else:
        return '.'

def dfs_cross(c,r):
    # check values
    if not_valid_coord(c,r): 
        return 0

    # very ugly logic, unsure how to do it better...
    # check 1 corner
    if check_match((c-1, r-1), (c-1,r+1)) == 'M':
        if check_match((c-1, r-1), (c+1,r-1)) == 'M':
            # more than 3 agree
            return 0
        else:
            if check_match((c+1, r-1), (c+1,r+1)) == 'S':
                return 1
    else:
        if check_match((c-1, r-1), (c+1,r-1)) == 'M':
            if check_match((c-1, r+1), (c+1,r+1)) == 'S':
                return 1
            else:
                return 0
        else:
            if check_match((c-1, r-1), (c-1,r+1)) == 'S':
                if check_match((c+1, r-1), (c+1,r+1)) == 'M':
                    return 1
            if check_match((c-1, r-1), (c+1,r-1)) == 'S':
                if check_match((c-1, r+1), (c+1,r+1)) == 'M':
                    return 1
    return 0

def main2():
    """Go through and check for A
    """
    ans = 0
    cols, rows = len(data), len(data[0])
    for c in range(cols):
        for r in range(rows):
            if data[c][r] != 'A':
                continue

            ans += dfs_cross(c,r)
    return ans
    

if __name__ == '__main__':
    print(f"part 1 = {main1()}")
    print(f"part 2 == {main2()}")