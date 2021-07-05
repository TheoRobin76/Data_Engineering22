# read lines and outputs list
# orders list
# test each individual function
# group into functions
# modular code

with open('slope') as slope:
    slope = slope.readlines()


# print('Slope', slope)


# slope = [line.replace("\n", '') for line in slope]
# print(slope)

def moving_through_trees(right, down):
    right_coord = 0
    down_coord = 0
    tree_counter = 0

    while down_coord < len(slope):
        if tree_at_coordinate(right_coord, down_coord):
            tree_counter += 1
        right_coord += right
        down_coord += down
    print(tree_counter)


def tree_at_coordinate(tree_x, tree_y):
    total_x = tree_x % 31
    return slope[tree_y][total_x] == '#'


moving_through_trees(1, 1)
moving_through_trees(3, 1)
moving_through_trees(5, 1)
moving_through_trees(7, 1)
moving_through_trees(1, 2)

