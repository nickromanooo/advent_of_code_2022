# https://adventofcode.com/2022/day/7



def part_one(file):
    f = open(file,'r')

    commands = f.read().strip().split('$ ')
    directory_sub_totals = {}
    directory_structure = {}
    dir_stack = ['/']
    for com in commands:
        com = com.strip()
        if len(com) == 0:
            continue

        if com[:2] == 'cd':
            _,dir = com.split()
            new_dir = com[3:].strip()
            old_dir = dir_stack[-1]
            if new_dir == old_dir:
                continue

            if new_dir == '..':
                if old_dir == '/':
                    continue
                dir_stack.pop()
            else :
                dir_stack.append(new_dir)
            # print(f'dir stack updated {dir_stack}')
            continue

        if com[:2] != 'ls':
            raise Exception(f'weird line? -{com}')

        outputs = com.split('\n')[1:]
        blargle = [x.split(' ') for x in outputs]
        sub_total = sum([int(y[0]) for y in blargle if y[0].isdigit()])
        sub_directories = [y[1] for y in blargle if y[0] == 'dir']

        directory_sub_totals['/'.join(dir_stack)] = sub_total
        if len(sub_directories) == 0:
            directory_structure['/'.join(dir_stack)] = []
        else:
            directory_structure['/'.join(dir_stack)] = ['/'.join(dir_stack + [x]) for x in sub_directories ]

    def get_directory_values(key):
        if key not in directory_structure:
            # print(f'key: {key}')
            return 0
        sub_dirs = directory_structure[key]
        if len(sub_dirs) == 0:
            return directory_sub_totals[key]

        return sum([get_directory_values(x) for x in sub_dirs]) + directory_sub_totals[key]

    selected_totals = [get_directory_values(d) for d in directory_structure.keys()]
    selected_totals = [x for x in selected_totals if x <= 100000]
    return sum(selected_totals)


def part_two(file):
    f = open(file,'r')

    commands = f.read().strip().split('$ ')
    directory_sub_totals = {}
    directory_structure = {}
    dir_stack = ['/']
    for com in commands:
        com = com.strip()
        if len(com) == 0:
            continue

        if com[:2] == 'cd':
            _,dir = com.split()
            new_dir = com[3:].strip()
            old_dir = dir_stack[-1]
            if new_dir == '/':
                continue

            if new_dir == '..':
                if old_dir == '/':
                    continue
                dir_stack.pop()
            else :
                dir_stack.append(new_dir)
            continue

        if com[:2] != 'ls':
            raise Exception(f'weird line? -{com}')

        outputs = com.split('\n')[1:]
        blargle = [x.split(' ') for x in outputs]
        sub_total = sum([int(y[0]) for y in blargle if y[0].isdigit()])
        sub_directories = [y[1] for y in blargle if y[0] == 'dir']

        directory_sub_totals['/'.join(dir_stack)] = sub_total
        if len(sub_directories) == 0:
            directory_structure['/'.join(dir_stack)] = []
        else:
            directory_structure['/'.join(dir_stack)] = ['/'.join(dir_stack + [x]) for x in sub_directories ]

    def get_directory_values(key):
        if key not in directory_structure:
            raise Exception(f'BAD KEY: {key}')
            return 0
        sub_dirs = directory_structure[key]
        if len(sub_dirs) == 0:
            return directory_sub_totals[key]

        return sum([get_directory_values(x) for x in sub_dirs]) + directory_sub_totals[key]

    selected_totals = [get_directory_values(d) for d in directory_structure.keys()]
    max = 70000000
    cur_filesystem_size = get_directory_values('/')
    selected_totals = [x for x in selected_totals if (cur_filesystem_size - x) <= 40000000 ]
    return sorted(selected_totals)[0]

print(f"Part one test: {part_one('test_input.txt')}")
print(f"Part one: {part_one('input.txt')}")
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}") # 8998590