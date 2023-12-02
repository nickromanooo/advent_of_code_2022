# https://adventofcode.com/2022/day/#
import math
def part_one(file):
    f = open(file,'r')
    lines = f.readlines()
    count = 0
    new_lines = []
    for i in range(len(lines)):
        line = [int(ch) for ch in lines[i].strip()]
        new_lines.append(line)
    lines = new_lines

    def is_visible(i,j,lines):
        if i == 0 or i == len(lines)-1:
            return True

        if j == 0 or j == len(lines)-1:
            return True

        val = lines[i][j]
        # calcs = [
        #     [char for char in lines[i][0:j]],
        #     [char for char in lines[i][j+1:]],
        #     [char for char in [lines[z][j] for z in range(0,i) ] ],
        #     [char for char in [lines[z][j] for z in range(len(lines)-1,i,-1) ] ],
        # ]

        return any(
            [
                all([char < val for char in lines[i][0:j]]),
                all([char < val for char in lines[i][j+1:]]),
                all([char < val for char in [lines[z][j] for z in range(0,i) ] ]),
                all([char < val for char in [lines[z][j] for z in range(len(lines)-1,i,-1) ] ]),
            ]
        )

    count = 0
    new_lines = [[-1 for _ in range(len(lines))] for _ in range(len(lines))]
    for i in range(len(lines)):
        for j in range(len(lines)):
            count += 1 if is_visible(i,j,lines) else 0

    return count


def part_two(file):
    f = open(file,'r')
    lines = f.readlines()
    count = 0
    new_lines = []
    for i in range(len(lines)):
        line = [int(ch) for ch in lines[i].strip()]
        new_lines.append(line)
    lines = new_lines

    def is_visible(i,j,lines):
        val = lines[i][j]
        score = 0

        direction_strings = [
            list(reversed(lines[i][0:j])),
            lines[i][j+1:],
            list(reversed([lines[z][j] for z in range(0,i) ])),
            [lines[z][j] for z in range(i+1,len(lines)) ],
        ]
        scores = []
        for d in direction_strings:
            score = 0
            for char in d:
                score += 1
                if char >= val:
                    break
            scores.append(score)

        return math.prod(scores)

    new_lines = [[is_visible(i,j,lines) for j in range(len(lines))] for i in range(len(lines))]
    count = max([max(line) for line in new_lines])


    return count

print(f"Part one test: {part_one('test_input.txt')}")
print(f"Part one: {part_one('input.txt')}") # 1870
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}") # 517440