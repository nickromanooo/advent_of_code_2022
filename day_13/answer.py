# https://adventofcode.com/2022/day/#
import ast
def part_one(file):
    f = open(file,'r')

    def make_list(item):
        if type(item) == list:
            return item
        return [item]

    def is_valid_compare(first,second):
        # print(f"    Comparing: {first} vs {second}")
        types = (type(first),type(second))
        if all([type == list for type in types]):
            # print("     All types were list")
            valid = None
            for i in range(max(len(first),len(second))):
                first_item,second_item = None,None
                try:
                    first_item = first[i]
                except:
                    # print(f"        Left side ran out == Valid")
                    return True
                try:
                    second_item = second[i]
                except:
                    # print(f"        Right side ran out == INvalid")
                    return False

                valid = is_valid_compare(first_item,second_item)
                if valid != None:
                    break
            return valid
        elif any([type == list for type in types]):
            # print("     One type was list")

            return is_valid_compare(make_list(first),make_list(second))

        # print("     Both were integers")
        if first == second:
            return None
        return first < second


    pairs = f.read().split('\n\n')
    valid_indexes = []
    for i in range(len(pairs)):
        pair = pairs[i].split()
        # print(f"== Pair {i+1} ==")
        first = ast.literal_eval(pair[0])
        second = ast.literal_eval(pair[1])
        valid = is_valid_compare(first,second)
        # print(f"Result was {valid}")
        if valid:
            valid_indexes.append(i+1)
    # print(valid_indexes)
    return sum(valid_indexes)


def part_two(file):
    f = open(file,'r')
    return

print(f"Part one test: {part_one('test_input.txt')}")
print(f"Part one: {part_one('input.txt')}")
# print(f"Part two test: {part_two('test_input.txt')}")
# print(f"Part two: {part_two('input.txt')}")