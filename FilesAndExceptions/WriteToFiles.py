def write_to_file(file, order_item):
    try:
        with open(file, 'a') as opened_file:
                opened_file.write(order_item + "\n")
    except FileNotFoundError:
        print("File cannot be found in directory")
        raise

write_to_file("orders.txt", "Chocolate Discs")


