# https://adventofcode.com/2022/day/3
import math
alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = alphabet + alphabet.upper()

def letter_value(letter):
    return alphabet.index(letter)+1

def part_one(file):
    f = open(file,'r')
    values = []
    for line in f.readlines():
        line = line.strip()
        if len(line) % 2 != 0:
            raise Exception(f'ODD LENGTH LINE: {line}')
        
        half = int(len(line)/2)

        rucksack_one = set(line[:half])
        rucksack_two = set(line[half:])
        rucksack_intersection = rucksack_one.intersection(rucksack_two)

        if len(rucksack_intersection) > 1:
            raise Exception(f'TOO MANY ITEMS FOUDN IN INTERSECTION: {rucksack_intersection}')
        
        letter = rucksack_intersection.pop()
        # print(f'{letter}: {letter_value(letter)}')
        values.append(letter_value(letter))
    return sum(values)

def part_two(file):
    f = open(file,'r')
    values = []
    groups = []
    for line in f.readlines():
        groups.append(line.strip())
        if len(groups) % 3 != 0:
            continue
        
        rucksack_one = set(groups[0])
        rucksack_two = set(groups[1])
        rucksack_three = set(groups[2])
        rucksack_intersection = rucksack_one.intersection(rucksack_two).intersection(rucksack_three)

        letter = rucksack_intersection.pop()
        # print(f'{letter}: {letter_value(letter)}')
        values.append(letter_value(letter))
        groups = []
    return sum(values)

# print(f"Part one test: {part_one('test_input.txt')}")
# print(f"Part one: {part_one('input.txt')}")#7428
print(f"Part two test: {part_two('test_input.txt')}")
print(f"Part two: {part_two('input.txt')}") #2650