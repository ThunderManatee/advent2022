from aocd import get_data
import re
data = get_data(day=5)
def crane(data, grabM):
  top = []
  crates, moves = data.split('\n\n')
  crates = crates.splitlines()
  moves = moves.splitlines()
  crates.pop()
  buckets = []
  for i in range(9):
    buckets.append([])
  for x in crates:
    for n, y in enumerate(re.findall('(?:[\w])|(?<= )\s{3}(?= )\s?', x)):
      if y.isalnum():
        buckets[n].append(y)
  for m in moves:
    move = re.findall('\d+', m)
    fromStack = int(move[1])-1
    toStack = int(move[2])-1
    for x in range(int(move[0])):
      mover = buckets[fromStack].pop(0)
      buckets[toStack].insert(x,mover) if grabM else buckets[toStack].insert(0,mover)
  for x in buckets:
    top.append(x[0])
  return top

print(crane(data,False))
print(crane(data,True))
