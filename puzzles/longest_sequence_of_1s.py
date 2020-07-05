# Given some bitstring b, you may change one bit from a 0 to a 1 in order to create the longest possible sequence of
# consecutive 1s. Output the length of the resulting longest sequence.
#
# Example: 11011101111
# Flipping the second 0 results in 11011111111, where the longest sequence of 1s is 8 long.
# Input
# Line 1: The bitstring b
# Output
# Line 1: The length of the longest possible sequence of 1s after flipping one bit
# Constraints
# 0 < number of bits in b < 1000
# b contains at least one 0
# Example
# Input
# 00
# Output
# 1

bits = input()

def checkseq(seq):
    return max(map(len, seq.split('0')))

l = []
for i, b in enumerate(bits):
    seq = bits
    if b=='0':
        seq=bits[:i]+'1'+bits[i+1:]
        l.append(checkseq(seq))

print(max(l))

# all in one line
print(max(max(map(len, (bits[:i]+'1'+bits[i+1:]).split('0'))) for i, b in enumerate(bits) if b=='0'))
