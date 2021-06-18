try:
    # file = open("order.txt") #saved and opened file, stored in variable "file"
    x = 4/0
except FileNotFoundError as errmsg:
    print("There has been an error! Panic") #this prints instead of the error
    print(errmsg)
except ZeroDivisionError as errmsg:
    print("You cannot divide by zero , you fool")
    print(errmsg)
    raise #shows the full error message



