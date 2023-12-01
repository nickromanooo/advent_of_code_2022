
def part_one():
    f = open('input.txt','r')
    elves = f.read().split('\n\n')
    elves = [[int(item) for item in elf.strip().split('\n')] for elf in elves]
    elf_sums = [sum(elf) for elf in elves]
    return max(elf_sums)

print(f"Part one: {part_one()}")

def part_two():
    f = open('input.txt','r')
    elves = f.read().split('\n\n')
    elves = [[int(item) for item in elf.strip().split('\n')] for elf in elves]
    elf_sums = sorted([sum(elf) for elf in elves], reverse=True)
    return sum(elf_sums[0:3])

print(f"Part one: {part_one()}")
print(f"Part two: {part_two()}")