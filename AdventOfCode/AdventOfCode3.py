#read lines and outputs list
#orders list
#test each individual function
#group into functions
#modular code
#read as one long bif string, every 34th is where you count. 3 across and 1 down is equal to 34 across

with open('slope') as slope:
    slope = slope.readlines()
# print('Slope', slope)
slope = [line.replace("\n", '') for line in slope]
print(slope)

