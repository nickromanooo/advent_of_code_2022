# https://adventofcode.com/2022/day/#

def part_one(file):
    f = open(file,'r')
    x = 1
    cycle = 0
    def signal_strength():
        return x * cycle

    #addx V
    #after two cycles the X register is increased by amount (can be negative)
    #noop takes one cycle to complete. does nothing
    lines = [line.strip() for line in f.readlines()]
    stop = False
    signal_strengths=[]
    buffer = None
    while len(lines):
        cycle += 1
        # print(f'--cycle {cycle}--')
        # print(f'    x: {x}  str: {signal_strength()}')
        if cycle % 40 == 20:
            signal_strengths.append((cycle,x,signal_strength()))

        while True:
            # do the buffered add
            if buffer:
                x += buffer
                # print(f'    cycle complete ADD BUFFER {buffer}')
                buffer = None
                break

            command = lines.pop(0)

            if command == 'noop':
                # print(f'    cycle complete NOOP')
                break

            _, val = command.split()

            buffer = int(val)
            # print(f'    cycle complete SET BUFFER {buffer}')
            break


        # print(f'    x: {x}  str: {signal_strength()}')

    return sum([_[2] for _ in signal_strengths])


def part_two(file):
    f = open(file,'r')
    x = 1
    cycle = 0
    def signal_strength():
        return x * cycle

    #addx V
    #after two cycles the X register is increased by amount (can be negative)
    #noop takes one cycle to complete. does nothing
    lines = [line.strip() for line in f.readlines()]
    stop = False
    signal_strengths=[]
    buffer = None
    crt_row = ''
    while len(lines):
        cycle += 1
        bonus = ' PIXEL' if abs(cycle-x) <= 1 else ''

        # print(f'--cycle {cycle} x {x} {bonus}--')

        #draw pixel
        pixel = cycle % 40
        if abs(pixel-x-1) <= 1:
            # print(f'    drawing #')
            crt_row += '#'
        else:
            crt_row += '.'
            # print(f'    drawing .')

        while True:
            # do the buffered add
            if buffer:
                x += buffer
                # print(f'    cycle complete ADD BUFFER {buffer}')
                buffer = None
                break

            command = lines.pop(0)

            if command == 'noop':
                # print(f'    cycle complete NOOP')
                break

            _, val = command.split()

            buffer = int(val)
            # print(f'    cycle complete SET BUFFER {buffer}')
            break
        # print(f'    row=: {crt_row}')

    # print(  f'==CRT==')
    while len(crt_row):
        print(crt_row[:40])
        crt_row = crt_row[40:]

    return sum([_[2] for _ in signal_strengths])

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}") 12520
# print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}")

####.#..#.###..####.###....##..##..#....
#....#..#.#..#....#.#..#....#.#..#.#...#
###..####.#..#...#..#..#....#.#....#...#
#....#..#.###...#...###.....#.#.##.#...#
#....#..#.#....#....#....#..#.#..#.#....
####.#..#.#....####.#.....##...###.####.