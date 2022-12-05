data = [ x.split(' ') for x in open('input.txt').read().splitlines() ]

guide = { 'A': 'R', 'B': 'P', 'C': 'S' }

score = { 'R': 1, 'P': 2, 'S': 3 }

win = { 'R': 'P', 'P': 'S', 'S': 'R' }
loose = { 'R': 'S', 'P': 'R', 'S': 'P' }

def choice(o, s):
  if s == 'Y':
    return o
  
  if s == 'X':
    return loose[o]
  
  if s == 'Z':
    return win[o]

def result(o, m):
  if o == m:
    return 3
  
  if (o == 'R' and m == 'S') or (o == 'S' and m == 'P') or (o == 'P' and m == 'R'):
    return 0
    
  return 6

def playround(opponent, m):
  o = guide[opponent]
  
  choice_points = score[m]
  
  result_points = result(o, m)
  
  points = choice_points + result_points
  
  return points
  
total = 0

for o, s in data:
  m = choice(guide[o], s)
  total += playround(o, m)
  
print(total)
