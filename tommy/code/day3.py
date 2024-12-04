
def is_valid_expression(string) -> bool:
    """bool if the submitted expression is valid under the string
    """
    if string[:4] != 'mul(':
        return False
    if string[-1] != ')':
        return False
    # between (,) needs to be a number 
    try:
        if ',' in string:
            num = string.split(',')
            # if not a num it'll return false from error checking 
            left_num = int(num[0].split('(')[-1])
            right_num = int(num[1].split(')')[0])
        else:
            return False
    except: 
        return False
    
    return True

def mult_flag(string):
    """Flag for if we keep the mult or not 
    """
    if string == "don't()":
        return False
    if string[0:4] == "do()":
        return True
    return None



def subset_string(string: str, switch: bool = False) -> str:
    """
    Get the expressions from the input string

    if switch is active, check if the do(), don't() indicator for whether or not to multiply
    """
    output = []
    left, right = 0,0
    expressions = []

    if switch:
        flag = True
    # 8 is the shortest expression it can be 
    while left <= len(string) - 8:
        switch_flag = mult_flag(string[left: left + 7])
        if switch_flag is not None:
            flag = switch_flag

        current_attempt = string[left: left + 4]
        # print(string[left: left + 4])
        if current_attempt == 'mul(':
            while right <= 8:
                # we're done if the next letter is longer than the string
                if left + 4 + right > len(string):
                    return expressions
            
                symbol_to_add = string[left + 4 + right]
                # if the next symbol isn't valid we leave
                if symbol_to_add not in '1234567890,)':
                    right = 0
                    break

                current_attempt += symbol_to_add

                # add the next letter to the current attempt
                if is_valid_expression(current_attempt):
                    if flag:
                        expressions.append(current_attempt)
                    right += 1
                    break
                right += 1
                
            # regardless we add index of mul( + however far right pointer got
            left += 4 + right
            right = 0
        else:
            left += 1

    return expressions

def evaluate_expression(mult_exp: str) -> int:
    """Given an expression string -> return value
    """
    num = mult_exp.split(',')
    left_num = int(num[0].split('(')[-1])
    right_num = int(num[1].split(')')[0])
    return left_num * right_num

        
def main1() -> int:
    """Given a string, parse for only valid keys in mult, then multiply them together and 
    add the parts
    """
    with open("tommy/txt_files/day3.txt") as f:
        string = f.read()

    exp_list = subset_string(string)

    return sum([evaluate_expression(exp) for exp in exp_list])

def main2() -> int:
    """This time we have a flag for whether or not the multiplication counts
    """
    with open("tommy/txt_files/day3.txt") as f:
        string = f.read()

    exp_list = subset_string(string, switch=True)

    return sum([evaluate_expression(exp) for exp in exp_list])

if __name__ == '__main__':
    print(f"Part 1 = {main1()}")
    print(f"Part 2 = {main2()}")    
