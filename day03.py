from aocd import get_data
data = get_data(day=3).splitlines()
priorityList = {chr(i+96):i for i in range(1,27)}
priorityList.update({chr(i+64):i+26 for i in range(1, 27)})

def part1(data):
    p = 0
    for x in data:
        c1 =  set(x[:len(x)//2])
        c2 = set(x[len(x)//2:])
        p = p + priorityList[''.join([match for match in c1 if w in c2])]
    return p

def part2(data):
    grouped = [data[n:n+3] for n in range(0, len(data), 3)]
    p = 0
    for g, h, i in grouped:
        p = p + priorityList[''.join([match for match in g if match in h and match in i][0])]
    return p

print(part1(data))
print(part2(data))
