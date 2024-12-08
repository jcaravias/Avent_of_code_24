from typing import List, Tuple, Dict
"""
We're given a list of conditions and a list of attempted solutions

reading through the attempt we need to confirm that it meets all the conditions
if it meets condition, save the middle value
else ignore
"""
def read_data() -> Tuple[list, list]:
    """input data, returning condition list and attempt list
    """
    with open("tommy/txt_files/day5.txt") as f:
        data = f.read().splitlines()

    conditions = []
    attempts = []
    flag = True
    for line in data:
        if line == '':
            flag = False
            continue
        if flag:
            conditions.append(line)
        else:
            attempts.append(line)
    return conditions, attempts
        

def parse_conditions(conditions: list) -> Tuple[dict, dict]:
    """Given list of conditions, parse them to create a boundary
    """
    prev_cond = {}
    post_cond = {}

    for condition in conditions:
        left_num, right_num = int(condition.split('|')[0]), int(condition.split('|')[1])
        prev_cond[right_num] = prev_cond.get(right_num, []) + [left_num]
        post_cond[left_num] = post_cond.get(left_num, []) + [right_num]

    return prev_cond, post_cond

def meet_condition(observed_list, condition_list):
    """
    checks if what we observe is different than what the condition says.
    if correct there should be no overlap between them
    """
    # if either are empty
    if not observed_list or not condition_list:
        return True
    
    for num in observed_list:
        if num in condition_list:
            return False
        
    return True 

def check_attempt(attempt: str, prev_cond: dict, post_cond: dict) -> int:
    """if solution is valid return middle index, else 0
    """
    for idx, value in enumerate(attempt):
        # get both sides of attempt
        left_of_current = attempt[:idx]
        right_of_current = attempt[idx+1:]
        # get our results of conditions
        necessary_prior = prev_cond.get(value,[])
        necessary_post = post_cond.get(value,[])
        # check that conditions are met
        if (
            not meet_condition(left_of_current, necessary_post) or 
            not meet_condition(right_of_current, necessary_prior)
            ): return 0
    # all conditions met
    return attempt[len(attempt)//2]
        
def fix_wrong_attempt(attempt, prev_cond, post_cond):
    """Reorder wrong attempt to be correct
    go through every element and move it to left until it is correct


    I think that I should go through each element starting left to right
    and adjust left until it is correct.

    """

    options = [i for i in attempt]
    for value in options:
        necessary_prior = prev_cond.get(value,[])
        while True:
            idx = attempt.index(value)
            right_of_current = attempt[idx+1:]
            # if this element is wrong
            if not meet_condition(right_of_current, necessary_prior):
                # then move the element 1 to the right
                attempt[idx], attempt[idx+1] = attempt[idx+1], attempt[idx]
            else:
                break # if this element is now correct
        try_success = check_attempt(attempt, prev_cond, post_cond)
        if try_success != 0:
            return try_success

            
def main1():
    conditions, attempts = read_data()

    prev_cond, post_cond = parse_conditions(conditions)

    ans = 0
    for attempt in attempts:
        attempt = attempt.split(',')
        attempt = [int(i) for i in attempt]
        
        ans += check_attempt(attempt, prev_cond, post_cond) 
    return ans

def main2():
    """for each incorrect from p1, fix them to be correct then add mid index
    """
    conditions, attempts = read_data()

    prev_cond, post_cond = parse_conditions(conditions)

    wrong_attempts = []
    for attempt in attempts:
        attempt = attempt.split(',')
        attempt = [int(i) for i in attempt]
        if not check_attempt(attempt, prev_cond, post_cond):
            wrong_attempts.append(attempt)
    ans = 0
    for attempt in wrong_attempts:
        ans += fix_wrong_attempt(attempt, prev_cond, post_cond)
    return ans

if __name__ == '__main__':
    print(f"Part 1 = {main1()}")
    print(f"Part 2 = {main2()}")
    
