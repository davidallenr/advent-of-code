def return_stack_count(lines):
    count_of_stacks = lines.strip().split(' ')[-1]

    return int(count_of_stacks)

def split_string(string) -> list:
    result = []
    try:
        for i in range(1, len(string), 4):
            result.append(string[i])
    except:
        pass

    return result

def move_boxes(count, from_pos, to_pos, crates_stack):
    for _ in range(count):
        # remove the top box from stack 'from_pos'
        box = crates_stack[from_pos].pop()
        # add the box to the top of stack 'to_pos'
        crates_stack[to_pos].append(box)



def move_boxes_with_crane(filename):
    # Read the sets from the file
    with open(filename) as f:
        crates_lines, move_lines = f.read().split("\n\n")
        count_of_stacks = return_stack_count(crates_lines)
        crates_lines = crates_lines.split("\n")
        move_lines = move_lines.split("\n")
        move_lines = [line.split(" ") for line in move_lines]

    indexes = []
    for i in enumerate(crates_lines[count_of_stacks-1]):
        #if the value at the index is not a space
        if i[1] != " ":
            indexes.append(i[0])

    del crates_lines[count_of_stacks - 1]
    #create a list of lists that is count_of_stacks long
    crates_stack = [[] for i in range(count_of_stacks)]

    for i, line in enumerate(crates_lines):
        for j, index in enumerate(indexes):
            if line[index] != " ":
                crates_stack[j].append(line[index])

    #reverse the elements of each list in crates_stack
    for i in range(len(crates_stack)):
        crates_stack[i].reverse()
        

    for line in move_lines:
        count = int(line[1])
        from_pos = int(line[3]) - 1
        to_pos = int(line[5]) - 1
        move_boxes(count, from_pos, to_pos, crates_stack)

    # create a new list containing the elements of crates_stack as strings
    crates_stack_strings = []
    for stack in crates_stack:
        print(f'stack: {stack}')
        crates_stack_strings.append("".join(stack.pop()))

    # concatenate the elements of crates_stack_strings into a single string
    crates_on_top_of_stacks = "".join(crates_stack_strings)

    return crates_on_top_of_stacks

# Test the function with the example data
print(move_boxes_with_crane('input.txt')) # should print CMZ