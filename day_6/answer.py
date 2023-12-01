# https://adventofcode.com/2022/day/#

def part_one(file):
    f = open(file,'r')
    line = f.read().strip()

    i = 0
    while i+4 < len(line):
        if len(set(line[i:i+4])) == 4:
            break
        i += 1
    return i+4

def part_two(file):
    f = open(file,'r')
    line = f.read().strip()
    
    offset=14
    i = 0
    while i+offset < len(line):
        if len(set(line[i:i+offset])) == offset:
            break
        i += 1
    return i+offset

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}") # 1361
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}") # 3263