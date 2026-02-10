test_list = [(5, 4, 2), (1, 3, 4), (5, 7, 8), (7, 4, 3)]
K=1
res = [abs(a[K]-y[K]) for a,y in zip(test_list,test_list[1:])]
print(res)