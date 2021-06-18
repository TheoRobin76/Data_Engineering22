import csv

with open("user_details.csv", newline='\n') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #delimiter isn't always a comma

    # print(csvreader)
    # for row in csvreader:
    #     print(row[-1]) #index to specify which part of the row to print

    # iterable_csv = iter(csvreader) #one way of removing the "email" column name
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row[-1])

    print(list(csvreader)) #prints the csv file as a list, duh

    counter = 0 #another way of removing the "email" column name
    for row in csvreader:
        if counter > 0:
            print(row[-1])
            counter += 1
        else:
            counter += 1


