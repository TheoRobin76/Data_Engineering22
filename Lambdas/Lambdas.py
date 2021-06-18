# def add(num1, num2):
#     return num1 + num2
#
# print(add(1,2))
#
# addition = lambda num1, num2: num1 + num2
#
# print(addition(2, 3))

saving = [234.00, 555.00, 674.00, 78.00]

# bonus = []
# for item in saving:
#     bonus.append(item*1.1)

bonus = list(map(lambda x: x*1.1, saving))

print(bonus)




