a = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
ele = 4
res = [tuple(i + ele for i in x) for x in a]
print(res)