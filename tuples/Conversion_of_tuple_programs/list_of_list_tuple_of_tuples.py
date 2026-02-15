test_list = [['Gfg', 'is', 'Best'], ['Gfg', 'is', 'love'],
             ['Gfg', 'is', 'for', 'Geeks']]

res = tuple(tuple(ele)for ele in test_list)
print(res)