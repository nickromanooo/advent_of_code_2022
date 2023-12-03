# https://adventofcode.com/2022/day/#
import re
import math
def part_one(file):
    f = open(file,'r')
    text = f.read()
    monkeys = {}
    monkey_ids = re.findall('(?<=Monkey\ )\d+',text)
    items = re.findall('(?<=Starting\ items:\ ).*',text)
    operations = re.findall('(?<=Operation:\ new\ \=\ old\ ).*',text)
    tests = re.findall('(?<=Test:\ divisible\ by\ )\d+',text)
    if_trues = re.findall('(?<=If\ true:\ throw to\ monkey\ )\d+',text)
    if_falses = re.findall('(?<=If\ false:\ throw to\ monkey\ )\d+',text)

    for i in range(len(monkey_ids)):
        monkeys[int(monkey_ids[i])] = {
            'items': [int(item) for item in items[i].split(', ')],
            'test': int(tests[i]),
            'operation': operations[i].split(),
            'if_true': int(if_trues[i]),
            'if_false': int(if_falses[i]),
        }
    # print(monkeys)
    rounds = 20
    monkey_counts = [0 for _ in range(len(monkeys))]
    for _ in range(rounds):
        for monkey_id,monkey in monkeys.items():
            # print(f'Monkey: {monkey_id}')
            while len(monkeys[monkey_id]['items']):
                level = monkeys[monkey_id]['items'].pop(0)
                monkey_counts[monkey_id] += 1
                # print(f'    Inspecting item with level {level}')
                operation_type = monkey["operation"][0]
                operation_value = int(monkey["operation"][1]) if monkey["operation"][1].isdigit() else level
                # do operation
                if operation_type == '+':
                    level = level + operation_value
                else:
                    level = level * operation_value

                # print(f'        operation= { operation_type} {operation_value} => {level}')
                # print(f'        testing {level} div {3}')

                level = level//3
                remainder = level % monkey['test']
                # print(f'        quotient {level} remainder {remainder}')

                if remainder == 0:
                    # print(f'        giving {level} to monkey {monkey["if_true"]}')
                    # print(monkeys[monkey['if_true']]['items'])
                    monkeys[monkey['if_true']]['items'].append(level)
                    # print(monkeys[monkey['if_true']]['items'])
                else:
                    # print(f'        giving {level} to monkey {monkey["if_false"]}')
                    # print(monkeys[monkey['if_false']]['items'])
                    monkeys[monkey['if_false']]['items'].append(level)
                    # print(monkeys[monkey['if_false']]['items'])

        # print(f'========= round results {_ + 1} ========')
        for monkey_id,monkey in monkeys.items():
            # print(f"    monkey {monkey_id}: {monkey['items']}")
            pass

    # for i in range(len(monkey_counts)):
    #     print(f'monkey {i}: {monkey_counts[i]}')

    print('MONKEY BUSINESS')
    monkey_counts = sorted(monkey_counts,reverse=True)

    return monkey_counts[0] * monkey_counts[1]


def part_two(file):
    f = open(file,'r')
    text = f.read()
    monkeys = {}
    monkey_ids = re.findall('(?<=Monkey\ )\d+',text)
    items = re.findall('(?<=Starting\ items:\ ).*',text)
    operations = re.findall('(?<=Operation:\ new\ \=\ old\ ).*',text)
    tests = re.findall('(?<=Test:\ divisible\ by\ )\d+',text)
    if_trues = re.findall('(?<=If\ true:\ throw to\ monkey\ )\d+',text)
    if_falses = re.findall('(?<=If\ false:\ throw to\ monkey\ )\d+',text)

    for i in range(len(monkey_ids)):
        monkeys[int(monkey_ids[i])] = {
            'items': [int(item) for item in items[i].split(', ')],
            'test': int(tests[i]),
            'operation': operations[i].split(),
            'if_true': int(if_trues[i]),
            'if_false': int(if_falses[i]),
        }
    # print(monkeys)
    rounds = 2
    monkey_counts = [0 for _ in range(len(monkeys))]
    tests = [monkey['test'] for monkey in monkeys.values()]
    for _ in range(rounds):
        for monkey_id,monkey in monkeys.items():
            # print(f'Monkey: {monkey_id}')
            while len(monkeys[monkey_id]['items']):
                level = monkeys[monkey_id]['items'].pop(0)
                if type(level) == int:
                    level = [level % test for test in tests]

                monkey_counts[monkey_id] += 1


                # # print(f'    Inspecting item with level {level}')
                operation_type = monkey["operation"][0]
                operation_value = monkey["operation"][1]
                # # do operation

                if operation_type == '+':
                    level = [x + int(operation_value) for x in level]
                else:
                    if monkey["operation"][1].isdigit():
                        level = [x * int(operation_value) for x in level]
                    else:
                        level = [x * x for x in level]

                for i in range(len(tests)):
                    level[i] = level[i] % tests[i]

                # 13 17 19 23
                # print(f'        operation= { operation_type} {operation_value} => {level}')
                # print(f'        testing {level} div {3}')


                #store products
                if level[monkey_id] == 0:
                    monkeys[monkey['if_true']]['items'].append(level)
                    # print(f'        giving {level} to monkey {monkey["if_true"]}')
                    # print(monkeys[monkey['if_true']]['items'])
                    # print(monkeys[monkey['if_true']]['items'])
                else:
                    # print(f'        giving {level} to monkey {monkey["if_false"]}')
                    # print(monkeys[monkey['if_false']]['items'])
                    monkeys[monkey['if_false']]['items'].append(level)
                    # print(monkeys[monkey['if_false']]['items'])

        print(f'========= round results {_ + 1} ========')
        for monkey_id,monkey in monkeys.items():
            print(f"    monkey {monkey_id}: {monkey['items']}")
            pass

    # for i in range(len(monkey_counts)):
    #     print(f'monkey {i}: {monkey_counts[i]}')

    print('MONKEY BUSINESS')
    monkey_counts = sorted(monkey_counts,reverse=True)

    return monkey_counts[0] * monkey_counts[1]
# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}")
print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two('input.txt')}")