from collections import Counter

test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]

res = [(*key,value) for key,value in Counter(test_list).items()]
print(res)
