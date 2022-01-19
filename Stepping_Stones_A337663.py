# #########################
# Sequence A337663 (https://oeis.org/A337663)
# or the Stepping Stones Puzzle 
# is a simple concept that is 
# very difficult to implement. 
# Start with n 1 tiles. Then 
# place n + 1 so that the sum 
# of the tiles around it are 
# equal to n + 1. Continue 
# until you cannot place the
# next tile. This is well 
# explained in the following 
# video by Numberphile video: 
# https://www.youtube.com/watch?v=m4Uth-EaTZ8.
#
# Code Written for efficiency.
# #########################

# Imports
from time import time

# Input
n = int(input("Number: "))

# Difference in Surrounding Coordinates
eight = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Return Coordinates of the Surrounding Tiles
def iterate_coord(coord, condition = lambda x:True):
    y, x = coord
    for y2, x2 in eight:
        if condition((y + y2, x + x2)):
            yield (y + y2, x + x2)

# Display Solutions
def show(grid):
    y, x = [*zip(*grid)]
    for y2 in range(min(y), max(y) + 1):
        for x2 in range(min(x), max(x) + 1):
            if (y2, x2) in grid:
                if grid[(y2, x2)] < 10:
                    print(grid[(y2, x2)], end = '  ')
                else:
                    print(grid[(y2, x2)], end = ' ')
            else:
                print('.', end = '  ')
        print()
    print()

# 12 Starting Positions
one_1     = {(1, 1): 1, (1, 2): 1, (2, 2): 2, (1, 3): 3}
s_one_1   = {(0, 0): 1, (0, 1): 2, (0, 2): 5, (0, 3): 4, (0, 4): 3, (1, 0): 1, (1, 4): 3, (2, 0): 1, (2, 1): 4, (2, 3): 6, (2, 4): 3, (3, 1): 2, (3, 2): 2, (3, 3): 2}
one_2     = {(1, 1): 1, (1, 2): 1, (2, 2): 2, (2, 3): 3}
s_one_2   = {(0, 0): 1, (0, 1): 2, (0, 2): 2, (0, 3): 1, (1, 0): 1, (1, 3): 6, (1, 4): 3, (2, 0): 1, (2, 1): 4, (2, 4): 3, (3, 1): 2, (3, 2): 5, (3, 3): 5, (3, 4): 3}
two_1     = {(1, 1): 1, (1, 3): 1, (2, 2): 2, (2, 1): 3}
s_two_1   = {(0, 0): 1, (0, 1): 1, (0, 2): 2, (0, 3): 1, (0, 4): 1, (1, 0): 4, (1, 2): 7, (1, 4): 1, (2, 0): 4, (2, 3): 3, (2, 4): 1, (3, 0): 3, (3, 1): 5, (3, 2): 5, (3, 3): 2}
three_1   = {(1, 1): 1, (2, 3): 1, (2, 2): 2, (2, 1): 3}
s_three_1 = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 4, (1, 2): 7, (1, 3): 3, (1, 4): 1, (2, 0): 4, (2, 4): 1, (3, 0): 3, (3, 1): 5, (3, 2): 6, (3, 3): 3, (3, 4): 1}
three_2   = {(1, 1): 1, (2, 3): 1, (2, 2): 2, (3, 2): 3}
s_three_2 = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 1, (1, 2): 4, (1, 3): 3, (1, 4): 1, (2, 0): 1, (2, 1): 6, (2, 4): 1, (3, 1): 5, (3, 3): 6, (3, 4): 1, (4, 1): 3, (4, 2): 3, (4, 3): 3}
three_3   = {(1, 1): 1, (2, 3): 1, (2, 2): 2, (3, 3): 3}
s_three_3 = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 1, (1, 2): 4, (1, 3): 3, (1, 4): 1, (2, 0): 1, (2, 1): 3, (2, 4): 4, (3, 1): 2, (3, 2): 6, (3, 4): 4, (4, 2): 3, (4, 3): 3, (4, 4): 3}
three_4   = {(1, 1): 1, (2, 3): 1, (2, 2): 2, (1, 3): 3}
s_three_4 = {(0, 0): 1, (0, 1): 1, (0, 2): 4, (0, 3): 3, (0, 4): 3, (1, 0): 1, (1, 2): 7, (1, 4): 4, (2, 0): 1, (2, 1): 3, (2, 4): 4, (3, 1): 2, (3, 2): 3, (3, 3): 3, (3, 4): 1}
four_1    = {(1, 1): 1, (3, 3): 1, (2, 2): 2, (1, 2): 3}
s_four_1  = {(0, 0): 1, (0, 1): 4, (0, 2): 4, (0, 3): 3, (1, 0): 1, (1, 3): 5, (2, 0): 1, (2, 1): 6, (2, 3): 6, (2, 4): 1, (3, 1): 2, (3, 2): 3, (3, 4): 1, (4, 2): 1, (4, 3): 1, (4, 4): 1}
five_1    = {(1, 1): 1, (1, 3): 1, (1, 2): 2, (2, 1): 3}
s_five_1  = {(0, 0): 1, (0, 1): 3, (0, 2): 4, (0, 3): 3, (0, 4): 1, (1, 0): 4, (1, 4): 1, (2, 0): 4, (2, 2): 7, (2, 3): 3, (2, 4): 1, (3, 0): 3, (3, 1): 3, (3, 2): 3}
five_2    = {(1, 1): 1, (1, 3): 1, (1, 2): 2, (2, 2): 3}
s_five_2  = {(0, 0): 1, (0, 1): 3, (0, 2): 4, (1, 0): 1, (2, 0): 1, (2, 1): 6, (0, 3): 3, (0, 4): 1, (1, 4): 1, (2, 3): 6, (2, 4): 1, (3, 1): 3, (3, 2): 3, (3, 3): 3}
six_1     = {(1, 1): 1, (2, 2): 1, (1, 2): 2, (3, 1): 3}
s_six_1   = {(0, 0): 1, (0, 1): 3, (0, 2): 3, (1, 0): 1, (2, 0): 4, (2, 1): 7, (1, 3): 3, (2, 3): 3, (3, 2): 4, (3, 3): 1, (0, 3): 2, (3, 0): 3, (4, 0): 3, (4, 1): 3, (4, 2): 3}
six_2     = {(1, 1): 1, (2, 2): 1, (1, 2): 2, (2, 3): 3}
s_six_2   = {(0, 0): 1, (0, 1): 3, (0, 2): 3, (0, 3): 2, (1, 0): 1, (1, 3): 6, (1, 4): 3, (2, 0): 1, (2, 1): 4, (2, 4): 3, (3, 1): 1, (3, 2): 4, (3, 3): 4, (3, 4): 3}

# Solve
def a(n):
    v_cur, s_cur = [one_1, one_2, two_1, three_1, three_2, three_3, three_4, four_1, five_1, five_2, six_1, six_2], [s_one_1, s_one_2, s_two_1, s_three_1, s_three_2, s_three_3, s_three_4, s_four_1, s_five_1, s_five_2, s_six_1, s_six_2]
    pos = 0
    num = 4

    while v_cur:
        v_prev, s_prev, v_cur, s_cur = v_cur, s_cur, [], []
        t = time()

        print(num, end = ' ')
        
        for q in range(len(v_prev)):
            values, sums = v_prev[q], s_prev[q]
            done = set()

            for num_coord in (k for k, v in sums.items() if v == num):
                if num_coord not in done:
                    if num_coord not in values:
                        temp_values = values.copy()
                        temp_sums = sums.copy()

                        temp_sums.update({add:temp_sums[add] + num if add in temp_sums else num for add in iterate_coord(num_coord)})

                        temp_values[num_coord] = num

                        pos += 1
                        v_cur.append(temp_values)
                        s_cur.append(temp_sums)
                        done.add(num_coord)
            
            if [*values.values()].count(1) < n:
                for num_coord in (k for k, v in sums.items() if v == num - 1):
                    if num_coord not in values:
                        for one_coord in iterate_coord(num_coord, condition = lambda x:x not in values and x not in sums and (num_coord, x) not in done):
                            temp_values = values.copy()
                            temp_sums = sums.copy()

                            temp_sums.update({add:temp_sums[add] + 1 if add in temp_sums else 1 for add in iterate_coord(one_coord)})
                            temp_sums.update({add:temp_sums[add] + num if add in temp_sums else num for add in iterate_coord(num_coord)})

                            temp_values[one_coord] = 1
                            temp_values[num_coord] = num
                            
                            pos += 1
                            v_cur.append(temp_values)
                            s_cur.append(temp_sums)
                            done.add((num_coord, one_coord))

        print(str(round(time() - t, 3)) + 's')
        num += 1

    print(pos, 'Positions')
    return v_prev

t2 = time()

# Grids and Sums of Grids
values, sums = [one_1, one_2, two_1, three_1, three_2, three_3, three_4, four_1, five_1, six_1, six_2], [s_one_1, s_one_2, s_two_1, s_three_1, s_three_2, s_three_3, s_three_4, s_four_1, s_five_1, s_six_1, s_six_2]

# Solve
for grid in a(n):
    show(grid)

print(str(round(time() - t2, 3)) + 's')
