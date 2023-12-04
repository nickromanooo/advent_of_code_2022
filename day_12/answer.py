# https://adventofcode.com/2022/day/#

def part_one(file):
    dead_moves = []

    f = open(file,'r')
    heightmap = [line.strip() for line in f.readlines()]
    new_heightmap = []
    start_pos = None
    end_pos = None
    for i in range(len(heightmap)):
        line = heightmap[i]
        new_line = []
        for j in range(len(line)):
            c = heightmap[i][j]
            if c == 'S':
                start_pos = (i,j)
                new_line.append(ord('a'))
            elif c == 'E':
                end_pos = (i,j)
                new_line.append(ord('z'))
            else:
                new_line.append(ord(c))
        new_heightmap.append(new_line)
    heightmap = new_heightmap
    cur_pos = start_pos
    dead_moves.append(start_pos)

    def valid_move(local_path,new_coord):
        try:
            return new_coord[0] >= 0 and new_coord[1] >= 0 and\
                coord_value(new_coord) - coord_value(local_path[-1]) < 2 and\
                coord_value(new_coord) - coord_value(local_path[-1]) > -1 and\
                new_coord not in dead_moves and\
                new_coord not in local_path
        except:
            return False

    def coord_value(coord):
        return heightmap[coord[0]][coord[1]]

    def possible_moves(local_path):
        coord = local_path[-1];
        maybe_moves = [
            (coord[0],coord[1]+1),
            (coord[0]+1,coord[1]),
            (coord[0]-1,coord[1]),
            (coord[0],coord[1]-1),
        ]
        return [
            x for x in maybe_moves if valid_move(local_path,x)
        ]

    def calc_paths_two(input_path):
        smallest_path = None
        paths = input_path
        while not smallest_path:
            new_paths = []
            for path in paths:
                if path[-1] == end_pos:
                    smallest_path = len(path)
                    break

                sub_paths = [path+[pm] for pm in possible_moves(path)]
                if not sub_paths:
                    continue
                # max_next = max([coord_value(p[-1]) for p in sub_paths])
                # optimal_sub_paths = [sp for sp in sub_paths if coord_value(sp[-1]) == max_next]
                # print(optimal_sub_paths)
                new_paths += sub_paths
            paths = new_paths
        return smallest_path

    smallest_path = calc_paths_two([[cur_pos]])
    return smallest_path-1


def part_two(file):
    f = open(file,'r')
    return

print(f"Part one test: {part_one('test_input.txt')}")
print(f"Part one: {part_one('input.txt')}")
# print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two('input.txt')}")