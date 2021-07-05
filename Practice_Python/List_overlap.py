from random import randrange
from random import randint
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# d = []
# for i in a:
#     if i in b:
#         d.append(i)
# print(d)

list1 = []
list2 = []
list3 = []
while len(list1) <= 20 and len(list2) <= 20:
    list1.append(randint(0, 100))
    list2.append(randint(0, 100))
print(f"List 1: {list1}")
print(f"List 2: {list2}")

for i in list1:
    if i in list2:
        list3.append(i)
print(f"List Overlap: {list3}")


