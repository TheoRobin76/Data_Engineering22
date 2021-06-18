# # def print_something(print_string):
# #     print(print_string)
# #
# # print_something("Banana House")
#
# def greeting(name: str) -> str:
#     print(f"Hello, my name is {name}")
#
# greeting(1231)
#
# # def addition(int1, int2):
# #     return int1+int2
# #
# # print(addition(4,9))
#
# # def multi_args(*multiargs):
# #     print(type(multiargs))
# #     for arg in multiargs:
# #         print(arg)
# #
# # multi_args(1,2,3,4,5,6,7,8,9)

def division(num: int, denom: int) -> float:
    return num/denom

print(division(3,2))

def subtraction(int1: int=5, int2: int=2) -> int:
    return int1 - int2

print(subtraction())