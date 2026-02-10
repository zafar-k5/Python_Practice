a = [(7, 8), (5, 6), (7, 5), (10, 4), (10, 1)]
res = sorted(a,key=lambda x:(-x[0],x[1]))
print(res)