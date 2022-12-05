data = [ sum([ int(y) for y in x.splitlines() ]) for x in open('input.txt').read().split("\n\n") ]
print(max(data))
