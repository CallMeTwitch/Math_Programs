# #########################
# The Collatz Conjecture is 
# well known in Mathematics 
# for being the simplest 
# problem that no one can 
# solve. The Problem? Start 
# with any number and if 
# it's even divide it by 
# two, otherwise multiply 
# it by 3 and add one. 
# Will it always end at 
# one or will some number 
# reach infinity? I 
# don't know but the 
# plots are pretty neat.
# 
# Code is written for 
# efficiency.
# #########################

from matplotlib import pyplot as plt
from tqdm import tqdm

# Get Range to Check, Make Memory
top_range = int(input('Top Range: '))
mem = [0] * (top_range + 1)

def collatz():
    for start in tqdm(range(2, top_range + 1)):
        # If mod(4) == 1: Value 2 or 3 Cached
        if start % 4 == 1:
            if ((3 * start) + 1) % 4:
                mem[start - 1] = mem[(((3 * start) + 1)//2)] + 2
            else:
                mem[start] = mem[(((3 * start) + 1)//4)] + 3
        # If mod(4) == 3: Use Algorithm
        elif start % 4 == 3:
            num = start
            count = 0
            while num >= start:
                if num % 2:
                    num = ((3 * num) + 1) // 2
                    count += 2
                else:
                    num //= 2
                    count += 1
            mem[start] = mem[num] + count
        # If mod(4) == 2 or 4: Value 1 Cached
        else:
            mem[start] = mem[(start // 2)] + 1

collatz()

# Plot each starting number with the length of it's sequence
plt.scatter([*range(1, len(mem) + 1)], mem, color = 'black', s = 1)
plt.show()
