data = [  [ int(i) for i in x.replace('-', ',').split(',') ] for x in  open('input.txt').read().splitlines() ]

count = 0

for x1,x2,x3,x4 in data:
  r1 = set(range(x1, x2+1))
  r2 = set(range(x3, x4+1))
  
  if set.intersection(r1, r2):
    count += 1

print(count)
