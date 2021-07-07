num = int(input("Please enter a number: "))
x = range(1, num + 1)

list1 = []
for i in x:
    if num % i == 0:
        list1.append(i)
        # print(len(list1))
if len(list1) == 2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
print(list1)
