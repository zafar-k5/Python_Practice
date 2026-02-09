a = [(1, 2), (3, 4, 5), (6,), (7, 8, 9, 10)]  
min_len, max_len = 2, 3  
res = [tup for tup in a if min_len <= len(tup) <= max_len]
print(res)