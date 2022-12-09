from math import copysign
from time import perf_counter

def get_data():
    with open('input.txt') as f:
        return [item.replace('\n', '') for item in f.readlines()]

def parse_move(item):
    direction, amount = item.split(' ')
    amount = int(amount)
    moves = [get_change(direction)]*amount
    return moves

def get_change(direction):
    if direction == 'R':
        return (1, 0)
    elif direction == 'U':
        return (0, 1)
    elif direction == 'L':
        return (-1, 0)
    elif direction == 'D':
        return (0, -1)

def build_move_set(data):
    move_set = []
    for item in data:
        move_set = move_set + parse_move(item)
    return move_set

def add_positions(pos1, pos2):
    return tuple(map(lambda i, j: i+j, pos1, pos2))

def diff_positions(pos1, pos2):
    return tuple(map(lambda i, j: i-j, pos1, pos2))

def determine_move(diff):
    return tuple(x if x == 0 else int(copysign(1, x)) for x in diff)

start_time = perf_counter()
data = get_data()
knots = [(0, 0) for x in range(10)]
all_tail_positions = []
move_set = build_move_set(data)
for idx, move in enumerate(move_set):
    for knot_index, knot_coords in enumerate(knots):
        # handle head movement differently than the rest
        if knot_index == 0:
            knots[knot_index] = add_positions(knots[knot_index], move)
            continue
        lead = knots[knot_index - 1]
        follow = knots[knot_index]
        diff = diff_positions(lead, follow)
        
        is_adjacent = max(tuple(map(lambda x: abs(x), diff))) <= 1
        if not is_adjacent:
            move = determine_move(diff)
            knots[knot_index] = add_positions(follow, move)
        all_tail_positions.append(knots[-1])
stop_time = perf_counter()
print('\n\nanswer:', len(set(all_tail_positions)), '\ntime:', stop_time - start_time)