input()  # skip
ln = input() or '0'

temps = [int(s) for s in ln.split()]

temps.sort(key = lambda x: (abs(x),-x))

print(temps)

print(temps[0])
