test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
res = sorted(test_list,key=lambda tup:sum([len(str(ele)) for ele in tup]))
print(res)