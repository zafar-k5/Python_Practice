test_list = [[(4, 5), (7, 8)], [(10, 13), (18, 17)]] 
tmp = [ele for sub in test_list for ele in sub]
res = zip(*tmp)
print(res)