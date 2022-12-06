import re

number_prog = re.compile(r"(\d+)")



stacks, procedure = [ x.splitlines() for x in open('input.txt').read().split('\n\n')]

stack_numbers = stacks[-1]

sn  = [ int(x) for x in number_prog.findall(stack_numbers) ]
maxstack = max(sn)

s = dict()

for i in sn:
  s[i] = []

for line in stacks[-2::-1]:
  for i in sn:
    p = -3 + 4 * i
    if line[p] != ' ':
      s[i].append(line[p])

for step in procedure:
  n, f, t  = [ int(x) for x in number_prog.findall(step) ]
  for i in range(n):
    s[t].append(s[f].pop())


print("".join([ s[i][-1] for i in sn ]))
