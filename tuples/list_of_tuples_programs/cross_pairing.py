test_list1 = [(1, 7), (6, 7), (9, 100), (4, 21)]
test_list2 = [(1, 3), (2, 1), (9, 7), (2, 17)]

res = [(tup1[1],tup2[1]) for tup1 in test_list1 for tup2 in test_list2 if tup1[0] == tup2[0]]
print(res)