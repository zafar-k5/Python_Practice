test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)

my_result = tuple(ele1 % elem2 for ele1, elem2 in zip(test_tup1,test_tup2))
print(my_result)