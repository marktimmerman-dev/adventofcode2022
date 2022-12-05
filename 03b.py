rucksacks = open('input.txt').read().splitlines()

groups = list(zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3]))

def prio(item):
  if item >= 'A' and item <= 'Z':
    return ord(item)-ord('A')+27
    
  return ord(item)-ord('a')+1

priorities = 0

for g1, g2, g3 in groups:
  common = list(set.intersection(set(g1), set(g2), set(g3)))[0]
  priorities += prio(common)
  
print(priorities)
