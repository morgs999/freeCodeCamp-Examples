def arithmetic_arranger(problems, show_answers=False):
    # initial error handling
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    ops = {
        '+': lambda pair: str(pair[0] + pair[1]),
        '-': lambda pair: str(pair[0] - pair[1]),
    }

    # initialize sets for lines
    first_set = []
    second_set = []
    third_set = []
    fourth_set = []
    arranged = []

    # loop through the given problems
    for problem in problems:
        # split problem into list
        new_item = problem.split(' ')

        # numbers for assigning spaces
        max_spaces = len(max(new_item, key=len))
        line_len = max_spaces + 2

        # pull individual items out
        strOne = new_item[0]
        strTwo = new_item[2]
        # error handling for length and type of operands
        if not all ([i.isnumeric() for i in new_item[::2]]):
            return 'Error: Numbers must only contain digits.'
        elif len(strOne) > 4 or len(strTwo) > 4:
            return 'Error: Numbers cannot be more than four digits.'


        oper = new_item[1]
        # error handling for weird operators
        if oper not in ops:
            return "Error: Operator must be '+' or '-'."
        if oper == '+':
            sumOf = str(int(new_item[0]) + int(new_item[2]))
        else:
            sumOf = str(int(new_item[0]) - int(new_item[2]))


        # format the first line
        first_num = new_item[0].rjust(line_len, ' ')
        first_set.append(first_num)

        # format the second line
        second_num = (f"{oper}{' ' * (line_len - len(strTwo) - 1)}{strTwo}")
        second_set.append(second_num)

        # format the third tline
        third_set.append('-'*(max_spaces+2))
       
       # format the fourth line if True
        if show_answers:
            res = ops[new_item[1]]([int(i) for i in new_item[::2]])
            fourth_set.append(f"{res.rjust(line_len, ' ')}")

        # end of for loop for problems


    # turn sets into lines
    arranged = '\n'.join(['    '.join(i) for i in (first_set, second_set, third_set)])

    if show_answers==True:
        arranged += '\n' + '    '.join(fourth_set)

    return arranged
    

###########################################
# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')


# print(repr(f'{}'))
# print(repr(''))