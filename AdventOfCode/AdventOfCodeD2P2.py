with open("day2text") as fp:
    file = fp.readlines()

# print(file)
valid_passwords = 0
# break original list into each password and policy
for line in file:
    count = 0
    data = line.split(", ")
# need to strip '\n' for each password
    for char in data:
        data = char.replace('\n', '')

        print("start")
        
        target = data[data.index(":") - 1]
        print(target)

        password = data.split(" ")[2]
        print(password)

        numbers = data.split(" ")[0]
        print(numbers)

        location2 = int(numbers.split("-")[1])
        print(f"location2: {location2}")

        location1 = int(numbers.split("-")[0])
        print(f"location1: {location1}")

        target1 = password[location1-1]
        print(f"target1 is {target1}")

        target2 = password[location2-1]
        print(f"target2 is {target2}")

        if target == target1 and target != target2:
                valid_passwords += 1
                print("valid_password")

        elif target != target1 and target == target2:
                valid_passwords += 1
                print("valid_password")

        else:
            print("Invalid password")

print(valid_passwords)