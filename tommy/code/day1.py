from typing import List, Tuple
from collections import Counter

def read_data() -> List:
    """Reads Txt file and roughly formats
    """
    with open("tommy/txt_files/day1.txt") as file:
        data = file.readlines()

    return [line.replace('\n','').replace('   ',',').split(',') for line in data]

def sort_data(data: List) -> Tuple[List[int], List[int]]:
    """Given data, return two sorted lists ascending
    """
    list1 = sorted([int(line[0]) for line in data])
    list2 = sorted([int(line[1]) for line in data])

    return list1, list2

def get_diff_between_locations(loc_1: List[int], loc_2: List[int]) -> int:
    """Given two sorted lists, return sum of differences
    """
    if len(loc_1) != len(loc_2):
        raise ValueError('Lists are not same size')
    
    return sum([abs(i-j) for i,j in zip(loc_1, loc_2)])

def calc_similarity_score(loc_1: List[int], loc_2: List[int]) -> int:
    """
    Calculate a total similarity score by adding up each number in the 
    left list after multiplying it by the number of times that number appears 
    in the right list.
    """
    # get count of second list
    count_list_2 = Counter(loc_2)
    list_1_ans = []
    for i in loc_1:
        # how many times its seen in second list
        times_seen = count_list_2[i]
        # mult element by # times seen
        list_1_ans.append(i * times_seen)
    
    return sum(list_1_ans)


def main1() -> int:
    """
    Given two columns of data, return the sum of differences between 
    them after being sorted
    """
    data = read_data()

    loc_1, loc_2 = sort_data(data)

    return get_diff_between_locations(loc_1, loc_2)

def main2() -> int:
    """
    Given two columns, return the sum of similarity score between two lists
    sim_score is defined as # times an element is contained in other list
    """
    data = read_data()

    loc_1, loc_2 = sort_data(data)

    return calc_similarity_score(loc_1, loc_2)


if __name__ == '__main__':
    
    print(f"Answer Part 1 = {main1()}")
    print(f"Answer Part 2 = {main2()}")