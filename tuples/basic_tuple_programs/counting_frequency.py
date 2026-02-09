from collections import Counter
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
res= dict(Counter(test_tup))
print(*res.values())