tup = ([5, 6], [6, 7, 8, 9], [3])
res = tuple(x for y in tup for x in y)
print(res)