from aocd import get_data
data = [x.split(',') for x in get_data(day=4).splitlines()]
a,b = 0,0
for x, y in data:
  xMin, xMax = [int(i) for i in x.split('-')]
  yMin, yMax = [int(j) for j in y.split('-')]
  if (xMin <= yMin and yMax <= xMax) or (yMin <= xMin and xMax <= yMax):
    a = a+1
  if (range(max(xMin, yMin), min(xMax, yMax)+1)):
    b = b+1
print(a,b)
  