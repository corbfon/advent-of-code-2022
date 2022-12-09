def get_data():
    with open('input.txt') as f:
        return [item.replace('\n', '') for item in f.readlines()]

def parse_move(line):
    split = line.split(' ')
    return {
        'qty': int(split[1]),
        'from': int(split[3]) - 1,
        'to': int(split[5]) - 1
    }

# stacks = [
#     ['Z', 'N'],
#     ['M', 'C', 'D'],
#     ['P']
# ]

stacks = [
    ['N', 'S', 'D', 'C', 'V', 'Q', 'T'],
    ['M', 'F', 'V'],
    ['F', 'Q', 'W', 'D', 'P', 'N', 'H', 'M'],
    ['D', 'Q', 'R', 'T', 'F'],
    ['R', 'F', 'M', 'N', 'Q', 'H', 'V', 'B'],
    ['C', 'F', 'G', 'N', 'P', 'W', 'Q'],
    ['W', 'F', 'R', 'L', 'C', 'T'],
    ['T', 'Z', 'N', 'S'],
    ['M', 'S', 'D', 'J', 'R', 'Q', 'H', 'N']
]



class shipyard:
    stacks = []
    move_multiple = False
    def __init__(self, stacks, move_multiple) -> None:
        self.stacks = stacks
        self.move_multiple = move_multiple


    def move(self, text):
        action = self._parse_move(text)
        pickup_crates = self.stacks[action['from']][-action['qty']:]
        if not self.move_multiple:
            pickup_crates.reverse()
        del self.stacks[action['from']][-action['qty']:]
        self.stacks[action['to']].extend(pickup_crates)

    def _parse_move(self, text):
        split = text.split(' ')
        return {
            'qty': int(split[1]),
            'from': int(split[3]) - 1,
            'to': int(split[5]) - 1
        }

    def top_row(self):
        row = [column[-1:][0] for column in self.stacks]
        return ''.join(row)

    def __str__(self):
        value = '---YARD---\n'
        stack_heights = [len(stack) for stack in self.stacks]
        max_height = max(stack_heights)
        for i in reversed(range(max_height)):
            for stack in self.stacks:
                if len(stack) >= i + 1 and stack[i]:
                    value += f'[{stack[i]}]'
                else:
                    value += '   '
            value += '\n'
        for i in range(len(self.stacks)):
            value += f' {i + 1} '
        value += '\n----------'
        return value
            



data = get_data()
yard = shipyard(stacks, True)
print(yard)
for item in data:
    yard.move(item, '')
    print(yard)


print('output', yard.top_row())
