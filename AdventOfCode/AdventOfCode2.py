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

        target = data[data.index(":") - 1]
        print(target)

        password = data[-1:data.index(":"):-1]
        print(password)

        numbers = data.split(" ")[0]
        print(numbers)

        maximum = int(numbers.split("-")[1])
        print(maximum)

        minimum = int(numbers.split("-")[0])
        print(minimum)

        for i in password:
            if i == target:
                count += 1
        print(f"target: {target} count: {count}")
        if count in range(minimum, maximum+1):
            valid_passwords += 1
            print("valid_passwords")
        else:
            print("Invalid password")

print(valid_passwords)


















# txt = "hello, my name is Peter, I am 26 years old"
# x = txt.split(", ")
# print(x)