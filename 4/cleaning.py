data = None

with open('input.txt') as f:
    data = [item.replace('\n', '').split(',') for item in f.readlines()]

def get_min_max(assignment):
    return [int(section) for section in assignment.split('-')]


total1 = 0
for pair in data:
    pair = [get_min_max(sect) for sect in pair]
    sections = pair[0] + pair[1]
    low = min(sections)
    high = max(sections)
    section_match = [section for section in pair if section[0] == low and section[1] == high]
    if (len(section_match) > 0):
        total1 += 1
    
print('section 1 total', total1)

total2 = 0
for pair in data:
    pair = [get_min_max(sect) for sect in pair]
    # sections = pair[0] + pair[1]
    # low = min(sections)
    # high = max(sections)
    # w1 = pair[0][1] - pair[0][0]
    # w2 = pair[1][1] - pair[1][0]
    # if w1 + w2 >= high - low:

    intersect = set(range(pair[0][0], pair[0][1] + 1)).intersection(range(pair[1][0], pair[1][1] + 1))
    if len(intersect) > 0:
        total2 += 1
    
print('section 2 total', total2)