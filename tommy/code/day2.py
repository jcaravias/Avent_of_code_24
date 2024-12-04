
def get_data():
    with open("tommy/txt_files/day2.txt") as file:
        data = file.read().split('\n')
        data = [i.split() for i in data]
    return [[int(i) for i in line] for line in data]

def is_monotonic(level):
    """Level is either all increasing or all decreasing 
    """
    return sorted(level, reverse=True) == level or sorted(level, reverse=False) == level

def adj_dist(level):
    """All adj index must differ between 1, 3 inclusive
    """
    for i in range(len(level) - 1):
        dist = abs(level[i+1] - level[i])
        if dist > 3 or dist < 1:
            return False
    return True 

def check_safety(level):
    """
    check if level is safe
    """
    return is_monotonic(level) and adj_dist(level)

def safe_after_deletion(level):
    """Given we can delete an element, is the list safe?
    """
    # go through the parts of each level
    for i in range(len(level)):
        new_level = level[:i] + level[i+1:]
        if check_safety(new_level):
            return True
    return False
            
def main1():
    """Count the number that are safe
    """
    levels = get_data()
    ans = 0
    for level in levels:
        if check_safety(level):
            ans += 1
    return ans

def main2():
    """If you could get rid of 1 element how many would be safe

    Only 1 exclusion at a time, otherwise we could've made a recursive soln.
    """
    levels = get_data()
    ans = 0
    for level in levels:
        if not check_safety(level) and not safe_after_deletion(level):
            continue
        ans += 1
    return ans
                
if __name__ == '__main__':
    print(f"num correct part 1 = {main1()}")
    print(f"num correct part 2 = {main2()}")