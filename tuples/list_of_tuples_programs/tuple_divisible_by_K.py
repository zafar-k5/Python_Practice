test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K = 6
result = [tup for tup in test_list if all(item % K == 0 for item in tup)]
print(result)