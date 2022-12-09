reindeer = []

with open('calories.txt') as f:
    data = [item.replace('\n', '') for item in f.readlines()]
    reindeer_sum = 0
    for item in data:
        if len(item) != 0:
            reindeer_sum += int(item)
        else:
            reindeer.append(reindeer_sum)
            reindeer_sum = 0
reindeer.sort(reverse=True)
print(sum(reindeer[0:3]))