import itertools

strengths = [5, 15, 17, 3,  8, 11, 28, 6, 55, 7]
strengths = sorted(strengths)
n = len(strengths)

print(min(abs(strengths[i]-strengths[i-1]) for i in range(n)))

print(min([abs(a-b) for a, b in itertools.combinations(strengths, 2)]))

