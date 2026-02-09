t1 = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
K = 1
result = [ele for ele in t1 if len(ele)!=K]
print(result)