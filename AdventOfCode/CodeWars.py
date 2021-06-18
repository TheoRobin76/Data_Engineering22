# def disemvowel(string):
#     new_string = ""
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for letter in string.lower():
#         if letter in vowels:
#             new_string = string.replace(letter, "")
#     return new_string
#
#
# print(disemvowel(houses))

# def gimme(input_array):
#     # Implement this function
#     for num in input_array:
#         if num < num and num > num3:
#             return input_array.index(num1)
#
# def get_count(input_str):
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     return input_str.count(str(vowels))
#
# get_count("houses")

data = "1-3 f: drgfffg"
data2 = "12-13 g: xgdfgfgfgfg"
data3 = "5-12 x: xwefwszzxzzzxxx"


# print(data.index("-"))

# to find minimum
# if "-" == data[1]:
#     mini = int(data[0])
# if "-" == data[2]:
#     mini = int(data[0] + data[1])

# to find minimum and maximum



# if '-' == data[1]:
#     minimum = int(data[0])
#     if ' ' == data[3]:
#         maximum = int(data[2])
#     elif ' ' == data[4]:
#         maximum = int(data[2] + data[3])
# elif '-' == data[2]:
#     minimum = int(data[0] + data[1])
#     if ' ' == data[5]:
#         maximum = int(data[3] + data[4])

data = "1-3 f: drgfffg"
data2 = "12-13 g: xgdfgfgfgfg"
data3 = "5-12 x: xwefwszzxzzzxxx"

# to find the target letter

target = (data3[data3.index(":")-1])
print(target)

# to find the password

password = data3[-1:data3.index(":"):-1]
print(password)

numbers = data3.split(" ")[0]
print(numbers)

password = data3.split(" ")[2]
print(password)

maximum = int(numbers.split("-")[1])
print(maximum)

minimum = int(numbers.split("-")[0])
print(minimum)




