test_list = [(5, 6, 7), (1, 3, 5), (8, 9, 19)]
K=2
res= ([sub[K] for sub in test_list])
product = 1
for item in res:
    product *= item
print(product)
    
