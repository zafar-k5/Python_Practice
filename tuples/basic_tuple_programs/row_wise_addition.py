test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
cus_eles = [6, 7, 8]

res = [[tup + (cus_eles[index], ) for tup in value] for index,value in enumerate(test_list)]
print(res)