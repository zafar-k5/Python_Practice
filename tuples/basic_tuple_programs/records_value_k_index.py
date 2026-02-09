test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
ele = 3
K = 1
res = list(filter(lambda x:x[K] == ele,test_list))
print(res)