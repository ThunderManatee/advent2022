from aocd import get_data
data = [x.split(' ') for x in get_data(day=2).splitlines()]

def part1(data):
    win = {'X': 'C', 'Y': 'A', 'Z': 'B'}
    lose = {'X': 'B', 'Y': 'Z', 'Z': 'A'}
    draw = {'X': 'A', 'Y': 'B', 'Z': 'C'}
    pts = {'X': 1, 'Y': 2, 'Z': 3}
    score = 0
    for e in data:
        score = score + pts[e[1]]
        if e[0] == draw[e[1]]:
            score = score + 3
        elif e[0] == win[e[1]]:
            score = score + 6 
    return score

def part2(data):
    theyChooseRock = {'X': 3, 'Y': 4, 'Z': 8}
    theyChoosePaper = {'X': 1, 'Y': 5, 'Z': 9}
    theyChooseScissors = {'X': 2, 'Y': 6, 'Z': 7}
    d = {'A': theyChooseRock, 'B': theyChoosePaper, 'C': theyChooseScissors}
    score = 0
    for e in data:
        ch = d[e[0]]
        score = score + (ch[e[1]])
    return score

print(part1(data))
print(part2(data))