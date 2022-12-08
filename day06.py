from aocd import get_data
data = get_data(day=6)
def part1(data):
    store = []
    for count, x in enumerate(data):
        store.append(x)
        if len(store) < 4:
            continue
        elif len(store) == 4 and (len(set(store)) == len(store)):
            return count+1
        else:
            store.pop(0)
def part2(data):
    store = []
    for count, x in enumerate(data):
        store.append(x)
        if len(store) < 14:
            continue
        elif len(store) == 14 and (len(set(store)) == len(store)):
            return count+1
        else:
            store.pop(0)

print(part1(data))
print(part2(data))