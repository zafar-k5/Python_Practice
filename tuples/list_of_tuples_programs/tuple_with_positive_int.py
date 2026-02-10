test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
result = [tup for tup in test_list if all(item >= 0 for item in tup)]
print(result)