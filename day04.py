from aocd import get_data
data = [x.split(',') for x in get_data(day=4).splitlines()]
pairs = 0
for x, y in data:
  xMin, xMax = [int(i) for i in x.split('-')]
  yMin, yMax = [int(j) for j in y.split('-')]
  xr = range(xMin, xMax)
  yr = range(yMin, yMax)
  if all(e in yr for e in xr) or all(e in xr for e in yr):
    pairs = pairs + 1
  print(xr, yr, pairs)