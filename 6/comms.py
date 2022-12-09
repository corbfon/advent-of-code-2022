def get_data():
    with open('input.txt') as f:
        return [item.replace('\n', '') for item in f.readlines()]

def get_start(data, unique_length):
    for i in range(len(data)):
        if i < unique_length:
            continue
        compare = data[i-unique_length:i]
        if len(compare) == len(set(compare)):
            return compare

        
data = get_data()[0]
length = 14
start = get_start(data, length)
answer = data.index(start) + length
print('the answer is', answer)