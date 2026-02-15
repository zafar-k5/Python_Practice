t = (1, 2, 3, 4)
res = tuple((t[i],t[i+1])for i in range(len(t)-1))
print(res)