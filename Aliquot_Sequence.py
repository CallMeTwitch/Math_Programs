# #########################
# The aliquot sequence is 
# the sequence of 
# nonnegative integers 
# with each term being the 
# sum of the proper 
# divisors of the previous 
# term. It is conjectured 
# that every sequence ends 
# in either 1 or a loop.
# 
# Code is written for
# efficiency.
# #########################

from primefac import primefac

# Returns the sum of the divisors of num ** power
def get_sum(num, power):
    output = num + 1
    temp = num ** 2

    while power - 1:
        output += temp
        temp *= num
        power -= 1
    return output

# Returns a list of the number is the Aliquot Sequence of num
def aliquot(num, mem):
    if num == 1:
        return mem + [1]
    if num in mem:
        return mem + [num]

    mem += [num]

    new = 1
    primes = []
    # Sum of Proper divisors = product of sum of divisors of prime factors
    for q in primefac(num):
        primes.append(q)
    for q in set(primes):
        new *= get_sum(q, primes.count(q))
    return aliquot(new - num, mem)

# Prints all the lists of sequences from 1-1000 (Excluding 13, they are too large for this program, exceeding 45 digit numbers)
for q in range(1, 1_000):
    if q not in [276, 306, 396, 552, 564, 660, 696, 780, 828, 840, 888, 966, 996]:
        print(f'{q} ~ {aliquot(q, [])}')