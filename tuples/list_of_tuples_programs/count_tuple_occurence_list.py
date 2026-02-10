from collections import defaultdict
Input = [[('hi', 'bye')], [('Geeks', 'forGeeks')],
         [('a', 'b')], [('hi', 'bye')], [('a', 'b')]]
my_dict = defaultdict(int)
for elem in Input:
    my_dict[elem[0]] += 1

print(*my_dict)