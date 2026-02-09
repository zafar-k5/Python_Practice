test_tup = (1, 5, 7, 8, 10) 

result = [x*y for x,y in zip(test_tup,test_tup[1:])]
print(result)