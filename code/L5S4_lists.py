# sort a list, remove last item, print the list
a_list = [1, 5, 4, 2, 3]
a_list.sort()
a_list.pop()
for x in a_list:
    print(x, end=" ")
