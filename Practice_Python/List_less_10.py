list1 = [1, 2, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for i in list1:
#     if i < 5:
#         print(i)

# list2 = []
# for i in list1:
#     if i < 5:
#         list2.append(i)
# print(list2)

# list2 = []
# num = int(input("Please choose a number: "))
# for i in list1:
#     if i < num:
#         list2.append(i)
# print(list2)

num = int(input("Please choose a number: "))
list2 = [x for x in list1 if x < num]
print(list2)
