# https://adventofcode.com/2022/day/6



def part_one(file):
    f = open(file,'r')

    lines = f.read().strip().split('$ ')
    directory = []
    directory_sub_totals = {}
    directory_structure = {}
    dir_stack = ['/']
    for line in lines:
        line = line.strip()
        if line[:2] == 'cd':
            new_dir = line[3:]
            old_dir = dir_stack[-1]
            if new_dir == old_dir:
                continue

            if new_dir == '..':
                if old_dir == '/':
                    continue
                dir_stack.pop(-1)
            else :
                dir_stack.append(new_dir)

            continue

        if line[:2] != 'ls':
            continue
        outputs = line.split('\n')[1:]
        commands = [x.split(' ') for x in outputs]
        sub_total = sum([int(y[0]) for y in commands if y[0].isdigit()])
        sub_directories = [y[1] for y in commands if y[0] == 'dir']
        directory_sub_totals[dir_stack[-1]] = sub_total
        if len(sub_directories) == 0:
            directory_structure[dir_stack[-1]] = []
        else:
            directory_structure[dir_stack[-1]] = sub_directories

    def get_directory_values(key):
        sub_dirs = directory_structure[key]
        if len(sub_dirs) == 0:
            return directory_sub_totals[key]
        
        return sum([get_directory_values(x) for x in sub_dirs]) + directory_sub_totals[key]

    # print(directory_sub_totals)
    print(len(directory_structure))
    print(directory_structure.keys())
    selected_totals = [get_directory_values(d) for d in directory_structure.keys()]
    selected_totals = [x for x in selected_totals if x <= 100000]

    print(f"/: {directory_structure['/']}")
    for key in directory_structure['/']:
        print(f'{key}: {directory_structure[key]}')
    return sum(selected_totals)


print(f"Part one test: {part_one('test_input.txt')}")
print(f"Part one: {part_one('input.txt')}")
# print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two('input.txt')}") # 3263