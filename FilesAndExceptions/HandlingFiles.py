# x = open("orders.txt", 'r') #read
# x = open("orders.txt", 'w') #writing - overwrites what is in file
# x = open("orders.txt", 'x') #delete
# x = open("orders.txt", 'a') #append - adds to end of the file - better than write
# x = open("orders.txt", 't') #text mode
# x = open("orders.txt", 'b') #binary
# x = open("orders.txt", '+') #read and write

def open_print_file(file):
    try:
        with open(file, 'r') as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("File cannot be found in the directory")
        raise
    finally:
        print("\nExecution complete")

open_print_file("orders.txt")


