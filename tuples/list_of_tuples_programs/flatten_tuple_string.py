test_list = [('1', '4', '6'), ('5', '8'), ('2', '9'), ('1', '10')]
res = " ".join([x for tup in test_list for x in tup])
print(res)