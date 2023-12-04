# https://adventofcode.com/2022/day/#
import ast
def part_one(file):
    f = open(file,'r')

    def is_valid_compare(first,second):
        return True
    
    pairs = f.read().split('\n\n')
    valid_indexes = []
    for i in range(len(pairs)):
        pair = pairs[i].split()
        first = ast.literal_eval(pair[0])
        second = ast.literal_eval(pair[1])
        valid = is_valid_compare(first,second)
        if valid:
            valid_indexes.append(i+1)
    print(valid_indexes)
    return sum(valid_indexes)


def part_two(file):
    f = open(file,'r')
    return

print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}")
# print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two('input.txt')}")