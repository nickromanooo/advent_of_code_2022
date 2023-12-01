# https://adventofcode.com/2022/day/5


def part_one(file):
    f = open(file,'r')
    f = f.read()
    crate_input,move_input = f.split('\n\n')
    moves = [[z[1],z[3],z[5]] for z in [y.split(' ') for y in [x for x in move_input.split('\n')]]]


    crates = crate_input.split('\n')
    crates = crates[:-1]
    crates = [crate[1::4] for crate in crates]
    new_crates = [[] for _ in range(len(crates[0]))]
    for crate in crates:
        for index in range(len(crate)):
            char = crate[index]
            if char == ' ':
                continue
            new_crates[index].append(char)
    crates = new_crates

    for move in moves:
        #move X from Y to Z
        move_count = int(move[0])
        move_from_index = int(move[1])-1
        move_to_index = int(move[2])-1
        # print(f'moving {move_count} crates from column {move_from_index} to {move_to_index}')

        for _ in range(move_count):
            crate_to_move = crates[move_from_index].pop(0)
            crates[move_to_index].insert(0,crate_to_move)

    return ''.join([crate[0] for crate in crates])


def part_two(file):
    f = open(file,'r')
    f = f.read()
    crate_input,move_input = f.split('\n\n')
    moves = [[z[1],z[3],z[5]] for z in [y.split(' ') for y in [x for x in move_input.split('\n')]]]


    crates = crate_input.split('\n')
    crates = crates[:-1]
    crates = [crate[1::4] for crate in crates]
    new_crates = [[] for _ in range(len(crates[0]))]
    for crate in crates:
        for index in range(len(crate)):
            char = crate[index]
            if char == ' ':
                continue
            new_crates[index].append(char)
    crates = new_crates

    for move in moves:
        #move X from Y to Z
        move_count = int(move[0])
        move_from_index = int(move[1])-1
        move_to_index = int(move[2])-1
        # print(f'moving {move_count} crates from column {move_from_index} to {move_to_index}')

        crates_to_move = crates[move_from_index][:move_count]
        crates[move_from_index] = crates[move_from_index][move_count:]
        crates[move_to_index] = crates_to_move + crates[move_to_index]

    return ''.join([crate[0] for crate in crates])

# print(f"Part one test: {part_one('test_input.txt')}") # CMZ
# print(f"Part one: {part_one('input.txt')}") # CVCWCRTVQ
print(f"Part two test: {part_two('test_input.txt')}") # MCD
print(f"Part two: {part_two('input.txt')}") # CNSCZWLVT