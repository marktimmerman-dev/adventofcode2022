rucksacks = open('input.txt').read().splitlines()

compartments = [ (x[:len(x)//2], x[len(x)//2:]) for x in rucksacks ]

def prio(item):
  if item >= 'A' and item <= 'Z':
    return ord(item)-ord('A')+27
    
  return ord(item)-ord('a')+1

priorities = 0

for c1, c2 in compartments:
  common = list(set.intersection(set(c1), set(c2)))[0]
  priorities += prio(common)
  
print(priorities)
