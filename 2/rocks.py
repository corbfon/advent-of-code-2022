# play_map = {
#     'X': {
#         'corresponds': 'A',
#         'points': 1,
#         'beats': 'C'
#     },
#     'Y': {
#         'corresponds': 'B',
#         'points': 2,
#         'beats': 'A'
#     },
#     'Z': {
#         'corresponds': 'C',
#         'points': 3,
#         'beats': 'B'
#     }
# }

play_map = [
    {
        'alpha': 'A',
        'name': 'Rock',
        'points': 1,
        'beats': 'Scissors'
    },
    {
        'alpha': 'B',
        'name': 'Paper',
        'points': 2,
        'beats': 'Rock'
    },
    {
        'alpha': 'C',
        'name': 'Scissors',
        'points': 3,
        'beats': 'Paper'
    }
]

with open('rocks.txt') as f:
    data = [item.replace('\n', '').split() for item in f.readlines()]
    total = 0
    for item in data:
        their_play_alpha, win_condition = item
        their_play = next(item for item in play_map if item['alpha'] == their_play_alpha)
        my_play = None
        win_points = 0
        if win_condition == 'Z':
            my_play = next(item for item in play_map if item['beats'] == their_play['name'])
            win_points = 6
        elif win_condition == 'Y':
            my_play = next(item for item in play_map if item['name'] == their_play['name'])
            win_points = 3
        else:
            my_play = next(item for item in play_map if item['name'] != their_play['name'] and item['beats'] != their_play['name'])
        play_points = my_play['points']
        
        print(f"win condition: {win_condition}. play: {their_play['name']} vs {my_play['name']}. Awarded {win_points} for win. Awarded {play_points} for play.")
        total += win_points + play_points

print(f'{total} points awarded')