t1 = (4, 5)
t2 = (7, 8)

result = [(a,b) for a in t1 for b in t2] + [(a,b) for a in t2 for b in t1]
print(result)
