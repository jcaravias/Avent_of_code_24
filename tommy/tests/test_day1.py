import pytest
import numpy as np
from tommy.code.day1 import *

def test_day_1_part1():
    assert main1() == 1879048

def test_day_1_part2():
    assert main2() == 21024792

def test_similarity_score():
    list1 = list2 = [1,2,3,4]
    assert calc_similarity_score(list1, list2) == sum([1,2,3,4])

    list1, list2 = [1,2,3,4], [1,2,3]
    assert calc_similarity_score(list1, list2) == sum([1,2,3])

    list1, list2 = [1,2,3,4], [1,2,3,3,3]
    assert calc_similarity_score(list1, list2) == sum([1,2,9])

def test_difference_calc():
    list1 = list2 = [1,2,3,4]
    assert get_diff_between_locations(list1, list2) == 0

    list1, list2 = [1,2,3,4], [5,4,3,2]
    assert get_diff_between_locations(list1, list2) == 8


