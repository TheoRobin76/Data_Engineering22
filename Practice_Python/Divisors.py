num = int(input("Please enter a number: "))
x = range(1, num + 1)
# for i in x:
# print(i)
list1 = []
for i in x:
    if num % i == 0:
        list1.append(i)
print(list1)
