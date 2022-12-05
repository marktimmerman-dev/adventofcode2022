data = [ sum([ int(y) for y in x.splitlines() ]) for x in open('input.txt').read().split("\n\n") ]
data.sort(reverse=True)
print(sum(data[:3]))
