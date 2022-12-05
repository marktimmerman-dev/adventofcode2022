data = [ x.split(' ') for x in open('input.txt').read().splitlines() ]

guide = { 'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S' }

score = { 'R': 1, 'P': 2, 'S': 3 }

def result(o, m):
  if o == m:
    return 3
  
  if (o == 'R' and m == 'S') or (o == 'S' and m == 'P') or (o == 'P' and m == 'R'):
    return 0
    
  return 6

def playround(opponent, me):
  o = guide[opponent]
  m = guide[me]
  
  choice_points = score[m]
  
  result_points = result(o, m)
  
  points = choice_points + result_points
  
  print(f"{opponent} {me} -> {o} {m} -> {choice_points} + {result_points} = {points}")

  return points
  
total = 0

for o, m in data:
  total += playround(o, m)
  
print()
print('total', total)
