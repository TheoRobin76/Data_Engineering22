# https://www.w3resource.com/python-exercises/lambda/index.php#EDITOR
# addition = lambda num1, num2: num1 + num2
#
# print(addition(2, 3))

#1
add = lambda num: num + 15
print(add(10))

multiply = lambda x, y: x * y
print(multiply(12, 4))


#2
def maths_function(n):
    return lambda x: x * n

result = maths_function(2)
print("Double the number of 15 =", result(15))
result = maths_function(3)
print("Triple the number of 15 =", result(15))
result = maths_function(4)
print("Quadruple the number of 15 =", result(15))
result = maths_function(5)
print("Quintuple the number of 15 =", result(15))


#3
tuples = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(tuples)
tuples.sort(key = lambda x: x[1])
print(tuples)


#4
dictionaries = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
 {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
 {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
print(dictionaries)
dictionaries.sort(key = lambda x: x['color'])
print(dictionaries)


#5
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)


#6
square = list(map(lambda x: x*x, nums))
print(square)
cube = list(map(lambda x: x*x*x, nums))
print(cube)




