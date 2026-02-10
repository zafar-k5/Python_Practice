from collections import Counter
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
print(tuple(Counter(test_tup).keys()))