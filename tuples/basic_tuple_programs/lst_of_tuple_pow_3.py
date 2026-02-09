# Input: [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]

a = [1, 2, 3, 4, 5]
my_tup_lst = [(x,x**3) for x in a]
print(my_tup_lst)