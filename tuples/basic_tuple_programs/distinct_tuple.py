from collections import Counter
test_tup = (1, 4, 5, 6, 1, 4)

res = max(Counter(test_tup).values()) == 1
print(res)