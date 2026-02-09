# Example
# a = [1, 2, 3]
# b = (4, 5)
# c = [6, 7]

# Adding b to a can produce [1, 2, 3, (4, 5)] or [1, 2, 3, 4, 5].
# Adding c to b can produce (4, 5, 6, 7)

a = [1, 2, 3] 
b = (4, 5)    
c = [6, 7]  

a.extend(b)
print(a)

bandc = b + tuple(c)
print(bandc)