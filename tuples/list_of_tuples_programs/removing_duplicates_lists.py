from collections import Counter
test_tup = ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
my_set = set()
res = [tup for tup in test_tup if not(tuple(tup) in my_set or my_set.add(tuple(tup)))]
print(res)