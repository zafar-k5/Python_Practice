# Input:
t = (2, 4, 3, 6, 8, 11, 1, 9)
k=2

my_lst = sorted(t)
min_k = my_lst[:k]
max_k = my_lst[-k:]

print(*min_k)
print(*max_k)
