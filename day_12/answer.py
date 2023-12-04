# https://adventofcode.com/2022/day/#

def part_one(file):
    dead_moves = set()

    f = open(file,'r')
    heightmap = [line.strip() for line in f.readlines()]
    start_pos = None
    for i in range(len(heightmap)):
        line = heightmap[i]
        for j in range(len(line)):
            c = heightmap[i][j]
            if c == 'S':
                heightmap[i] = heightmap[i].replace('S','a')
                end_pos = (i,j)
            elif c == 'E':
                start_pos = (i,j)
                heightmap[i] = heightmap[i].replace('E','z')
    cur_pos = start_pos

    def valid_move(coord,new_coord):
        try:
            return new_coord[0] >= 0 and new_coord[1] >= 0 and\
                coord_value(new_coord) - coord_value(coord) > -2 and\
                new_coord not in dead_moves
        except:
            return False

    def coord_value(coord):
        return ord(heightmap[coord[0]][coord[1]])


    def possible_moves(coord):
        coord
        maybe_moves = [
            (coord[0]+1,coord[1]),
            (coord[0]-1,coord[1]),
            (coord[0],coord[1]+1),
            (coord[0],coord[1]-1)
        ]
        
        maybe_moves = [
            x for x in maybe_moves if valid_move(coord,x)
        ]
        return maybe_moves

    def calc_paths_wide(input_path):
        smallest_path = None
        paths = input_path
        step = 0 
        print(f"starting: {start_pos} ending: {end_pos}")
        while not smallest_path:
            step += 1
            new_paths = []
            dead_moves = [paths[-1]]
            for path in paths:
                if path == end_pos:
                    smallest_path = step
                    break
                dead_moves.append(path)
                sub_paths = [pm for pm in possible_moves(path)]
                if not sub_paths:
                    continue
                new_paths += sub_paths
            paths = list(set(new_paths))
        return smallest_path

    # IDEA
    # STORE CAN MOVE UP DOWN LEFT RIGHT FOR EACH ITEM/ROW

    smallest_path = calc_paths_wide([cur_pos])
    return smallest_path-1


def part_one(file):
    dead_moves = set()

    f = open(file,'r')
    heightmap = [line.strip() for line in f.readlines()]
    start_pos = None
    for i in range(len(heightmap)):
        line = heightmap[i]
        for j in range(len(line)):
            c = heightmap[i][j]
            if c == 'S':
                heightmap[i] = heightmap[i].replace('S','a')
                end_pos = (i,j)
            elif c == 'E':
                start_pos = (i,j)
                heightmap[i] = heightmap[i].replace('E','z')
    cur_pos = start_pos

    def valid_move(coord,new_coord):
        try:
            return new_coord[0] >= 0 and new_coord[1] >= 0 and\
                coord_value(new_coord) - coord_value(coord) > -2 and\
                new_coord not in dead_moves
        except:
            return False

    def coord_value(coord):
        return ord(heightmap[coord[0]][coord[1]])


    def possible_moves(coord):
        coord
        maybe_moves = [
            (coord[0]+1,coord[1]),
            (coord[0]-1,coord[1]),
            (coord[0],coord[1]+1),
            (coord[0],coord[1]-1)
        ]
        
        maybe_moves = [
            x for x in maybe_moves if valid_move(coord,x)
        ]
        return maybe_moves

    def calc_paths_wide(input_path):
        smallest_path = None
        paths = input_path
        step = 0 
        print(f"starting: {start_pos} ending: {end_pos}")
        while not smallest_path:
            step += 1
            new_paths = []
            dead_moves = [paths[-1]]
            for path in paths:
                if coord_value(path) == coord_value(end_pos):
                    smallest_path = step
                    break
                dead_moves.append(path)
                sub_paths = [pm for pm in possible_moves(path)]
                if not sub_paths:
                    continue
                new_paths += sub_paths
            paths = list(set(new_paths))
        return smallest_path

    # IDEA
    # STORE CAN MOVE UP DOWN LEFT RIGHT FOR EACH ITEM/ROW

    smallest_path = calc_paths_wide([cur_pos])
    return smallest_path-1
print(f"Part one test: {part_one('test_input.txt')}")
print(f"Part one: {part_one('input.txt')}")
# print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two('input.txt')}")