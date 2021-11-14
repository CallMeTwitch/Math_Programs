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

num = int(input('Starting Number: '))

mem = [0]

# Edits mem in place, appending the length of each collatz sequence
def collatz(num, count = 0):
    if num < q:
        mem.append(mem[num - 1] + count)
    elif num % 2:
        collatz(((3 * num) + 1) // 2, count + 2)
    else:
        collatz(num // 2, count + 1)

# Fill mem
for q in tqdm(range(2, num + 1)):
    collatz(q)

# Plot each starting number with the length of it's sequence
plt.scatter([*range(1, len(mem) + 1)], mem, color = 'black', s = 1)
plt.show()