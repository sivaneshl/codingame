# The rule here is that you start with an element A1, and whenever you get to a number you have not seen before, the following term is a 0. But if the number An has appeared previously in the sequence, then you count the number of terms since the last appearance of An, and that number is the following term.
#
# For a series starting with A1 as 0, the series will be:
#
# 0, 0, 1, 0, 2, 0, 2, 2, 1, 6, 0, 5, 0, 2, 6, 5, 4, 0, 5, 3, 0, 3, …
#
# Term 1: The first term is 0.
# Term 2: Since we haven’t seen 0 before, the second term is 0.
# Term 3: Since we have seen a 0 before, one step back, the third term is 1
# Term 4: Since we haven’t seen a 1 before, the fourth term is 0
# Term 5: Since we have seen a 0 before, two steps back, the fifth term is 2.
#
# And so on...
# Input
# Line 1: a single integer A1 that is the first element in the sequence.
# Line 2: an integer N representing the nth position of an element in the sequence that is to be displayed as output.
# Output
# A single integer that is the Nth element of the sequence
# Constraints
# 0 ≤ A1 ≤ 200
# 1 ≤ N ≤ 1000000
# Example
# Input
# 0
# 2
# Output
# 0

import time

a1 = int(input())
n = int(input())

start = time.time()

seen = {}
# seq = [a1]
nbr = a1
for i in range(1, n):
    # print(i, nbr, seen)
    if nbr not in seen:
        # print('not seen')
        # seq.append(0)
        a1=0
    else:
        # print('seen')
        # seq.append(i-seen[nbr])
        a1=i-seen[nbr]
    seen[nbr] = i
    # nbr = seq[-1]
    nbr=a1
    # print('seen {}'.format(i), seen)
    # print('seq {}'.format(i), seq)

# print('final=', seq)
# print(seq[-1])
print(nbr)
end = time.time()
print(time.strftime("%H:%M:%S",time.gmtime(end-start)))