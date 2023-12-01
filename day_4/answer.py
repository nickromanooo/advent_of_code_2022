# https://adventofcode.com/2022/day/#

def part_one(file):
    f = open(file,'r')
    result = 0
    for line in f:
        line = line.strip()
        first,second = line.split(',')
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]


        if (first[0] <= second[0] and first[1] >= second[1]) or \
            (second[0] <= first[0] and second[1] >= first[1]):
            result += 1
        
    return result


def part_two(file):
    f = open(file,'r')
    result = 0
    for line in f:
        line = line.strip()
        first,second = line.split(',')
        first = [int(x) for x in first.split('-')]
        second = [int(x) for x in second.split('-')]


        if (first[0] <= second[0] and first[1] >= second[0]) or \
            (second[0] <= first[0] and second[1] >= first[0]):
            result += 1
        
    return result

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}")
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}")