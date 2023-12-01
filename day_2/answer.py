# a,x rock 1
# b,y paper 2
# c,z scissors 3

# 0 for loss, 3 for draw, 6 for win


# 1 beats 3
# 2 beats 1
# 3 beats 2

def part_one():
    score_map = {
        'A':1,
        'X':1,

        'B':2,
        'Y':2,

        'C':3,
        'Z':3
    }
    f = open('input.txt','r')
    rounds = []
    for line in f.readlines():
        them, me = line.strip().split(' ')
        them, me = score_map[them], score_map[me]
        score = me
        result = 'loss'
        if me == them:
            score += 3 # draw
            result = 'draw'
        elif (me == 1 and them == 3)\
              or (me == 2 and them == 1)\
              or me == 3 and them == 2:
            score += 6 # I win
            result = 'win'

        # print(f'me: {me} them: {them} score: {score} result: {result}')
        rounds.append(score)

    return sum(rounds)

def part_two():
    score_map = {
        'A':1,
        'X':1,
        'B':2,
        'Y':2,
        'C':3,
        'Z':3
    }
    # win loss draw
    win_map = {
        'A': {
          'X':'C', #lose
          'Y':'A', #draw
          'Z':'B', #win
        },
        'B': {
          'X':'A', #lose
          'Y':'B', #draw
          'Z':'C', #win
        },
        'C': {
          'X':'B', #lose
          'Y':'C', #draw
          'Z':'A', #win
        },
    }
    f = open('input.txt','r')
    rounds = []
    for line in f.readlines():
        them, desired_result = line.strip().split(' ')
        me = win_map[them][desired_result]
        me,them = score_map[me],score_map[them]
        score = me
        result = 'loss'
        if me == them:
            score += 3 # draw
            result = 'draw'
        elif (me == 1 and them == 3)\
              or (me == 2 and them == 1)\
              or me == 3 and them == 2:
            score += 6 # I win
            result = 'win'

        # print(f'me: {me} them: {them} score: {score} result: {result}')
        rounds.append(score)

    return sum(rounds)

print(f'part one: {part_one()}')#14297
print(f'part two: {part_two()}')#10498