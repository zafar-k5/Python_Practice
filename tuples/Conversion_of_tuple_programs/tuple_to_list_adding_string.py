test_tup = (5, 6, 7)
K = "Gfg"
res = [ele for sub in test_tup for ele in (sub, K)]
print(res)