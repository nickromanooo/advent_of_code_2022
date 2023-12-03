# https://adventofcode.com/2022/day/#
import math

def part_one(file):
    f = open(file,'r')
    head = (0,0)
    tail = (0,0)
    tail_positions = set([(0,0)])

    def maybe_move_tail(head,tail):
        x_distance = head[0]-tail[0]
        y_distance = head[1]-tail[1]

        abs_x_distance = abs(x_distance)
        abs_y_distance = abs(y_distance)

        if abs_x_distance <= 1 and abs_y_distance <= 1:
            return tail

        #lateral move
        if min(abs_x_distance,abs_y_distance) == 0:
            x_tail_move = int(x_distance/2)
            y_tail_move = int(y_distance/2)
        else:
            x_tail_move = 1 if x_distance > 0 else -1
            y_tail_move = 1 if y_distance > 0 else -1

        tail = (tail[0]+x_tail_move,tail[1]+y_tail_move)
        tail_positions.add(tail)
        return tail

    for line in f.read().splitlines():
        direction,distance = line.split(' ')
        # print(f'moving: {direction} => {distance}')

        # todo dont repeat yourself
        if direction in ['R','L']:
            modifier = -1 if direction == 'L' else 1
            for _ in range(int(distance)):
                head = (head[0]+modifier,head[1])
                tail = maybe_move_tail(head,tail)
        else:
            modifier = -1 if direction == 'D' else 1
            for _ in range(int(distance)):
                head = (head[0],head[1]+modifier)
                tail = maybe_move_tail(head,tail)


    return len(tail_positions)


def part_two(file):
    f = open(file,'r')
    tail_positions = set([(0,0)])
    rope_state = [(0,0) for x in range(10)]

    def maybe_move_tail(head,tail):
        x_distance = head[0]-tail[0]
        y_distance = head[1]-tail[1]

        abs_x_distance = abs(x_distance)
        abs_y_distance = abs(y_distance)

        if abs_x_distance <= 1 and abs_y_distance <= 1:
            return tail

        #lateral move
        if min(abs_x_distance,abs_y_distance) == 0:
            x_tail_move = int(x_distance/2)
            y_tail_move = int(y_distance/2)
        else:
            x_tail_move = 1 if x_distance > 0 else -1
            y_tail_move = 1 if y_distance > 0 else -1

        tail = (tail[0]+x_tail_move,tail[1]+y_tail_move)
        return tail

    for line in f.read().splitlines():
        direction,distance = line.split(' ')
        # print(f'moving: {direction} => {distance}')

        # todo dont repeat yourself
        modifier_x = 0
        modifier_y = 0
        if direction in ['R','L']:
            modifier_x = -1 if direction == 'L' else 1
            modifier_y = 0
        else:
            modifier_y = -1 if direction == 'D' else 1
            modifier_x = 0

        for d in range(int(distance)):
            rope_state[0] = (rope_state[0][0]+modifier_x,rope_state[0][1]+modifier_y)

            for e in range(0, len(rope_state)-1):
                rope_state[e+1] = maybe_move_tail(rope_state[e],rope_state[e+1])

                if e == len(rope_state)-2:
                    tail_positions.add(rope_state[e+1])


    return len(tail_positions)

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}") #6384
print(f"Part two test: {part_two('test_input_2.txt')}")
print(f"Part two: {part_two('input.txt')}") #2734