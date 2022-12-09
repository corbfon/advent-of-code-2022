from string import ascii_lowercase, ascii_uppercase
data = None
alpha = list(ascii_lowercase + ascii_uppercase)

with open('input.txt') as f:
    data = [item.replace('\n', '') for item in f.readlines()]

# part 1
total1 = 0
for sack in data:
    comp1, comp2 = [sack[:len(sack)//2], sack[len(sack)//2:]]
    match = next(item for item in comp1 if item in comp2)
    total1 += alpha.index(match) + 1

print('part 1 total', total1)

# part 2
def group_sacks(sacks):
    sacks_per_group = 3
    for i in range(0, len(sacks), sacks_per_group):
        yield sacks[i:i + sacks_per_group]

total2 = 0
groups = list(group_sacks(data))
for group in groups:
    badge = None
    for item in group[0]:
        if item in group[1] and item in group[2]:
            badge = item
    total2 += alpha.index(badge) + 1

print('part 2 total', total2)
    