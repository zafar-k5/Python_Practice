test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
res = [tup for tup in test_list if all(ele != None for ele in tup)]
print(res)