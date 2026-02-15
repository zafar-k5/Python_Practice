test_list = [[4, 5], [7, 3]]; add_list = ['Gfg', 'best'] 
res = []
for lst_item, add_item in zip(test_list,add_list):
    for item in lst_item:
        res.append((add_item,item))

print(res)