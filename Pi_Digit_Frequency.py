# #########################
# Pi is an irrational 
# number which means it's 
# decimal digits repeat 
# infinitely without any 
# pattern. I was curious 
# to see whether or not 
# they were represented 
# equally.
# 
# Code is written for
# readability.
# #########################

from mpmath import mp
import sys

# Set decimals of Pi to check and the number of bars to use in graph
mp.dps = 100_001
bars = 180

# Frquency dictionary
freq = {q:0 for q in range(10)}

digits = 0
# Iterate Digits
for q in str(mp.pi)[2:]:
    
    # Update Frequency
    freq[int(q)] += 1
    digits += 1

    # For line in previous output: Remove
    for _ in range(11): 
        sys.stdout.write("\x1b[1A\x1b[2K")

    # Make string of current output
    output = f'π || {digits}\n'
    for num in freq:
        t = int((freq[num] / max(bars, max(freq.values()))) * bars)
        output += f'{num} || {("=" * t) + (" " * (bars - t)) + " || "}{num}\n'
    # Print
    sys.stdout.write(output)