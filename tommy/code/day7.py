def calculate1(nums):
    if len(nums) == 1:
        return nums
    # this gradually shortens the problem over time. 
    # either we can *, +, concatenate the string of the numbers
    return (calculate1([nums[0] + nums[1]] + nums[2:]) +  # add
            calculate1([nums[0] * nums[1]] + nums[2:])) # multiply

def calculate2(nums):
    if len(nums) == 1:
        return nums
    # this gradually shortens the problem over time. 
    # either we can *, +, concatenate the string of the numbers
    return (calculate2([nums[0] + nums[1]] + nums[2:]) +  # add
            calculate2([nums[0] * nums[1]] + nums[2:]) + # multiply
            calculate2([int(str(nums[0]) + str(nums[1]))] + nums[2:]))  # concatenate


# read input_data from file
with open("tommy/txt_files/day7.txt") as file:
  input_data = file.readlines()

def main1():
    total = 0
    for line in input_data:
        left, right = line.split(": ")
        test_value = int(left)
        operands = list(map(int, right.split()))

        # get results of all possible operand/operator combinations
        results = calculate1(operands)
        # if one of the possible results is correct
        if test_value in results:
            total += test_value  # add it to the total
    return total

def main2():
    total = 0
    for line in input_data:
        left, right = line.split(": ")
        test_value = int(left)
        operands = list(map(int, right.split()))

        # get results of all possible operand/operator combinations
        results = calculate2(operands)
        # if one of the possible results is correct
        if test_value in results:
            total += test_value  # add it to the total
    return total

if __name__ == '__main__':
    print(f"part 1 = {main1()}")
    print(f"part 2 = {main2()}")