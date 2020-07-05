painted_sections, unpainted_sections = [], []
l, n = int(input()), int(input())
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    painted_sections.append((st, ed))
painted_sections = sorted(painted_sections)

for i, (st, ed) in enumerate(painted_sections):
    if i > 0 and painted_sections[i - 1][1] > ed > st:
        painted_sections[i] = painted_sections[i - 1]

for i, (st, ed) in enumerate(painted_sections):
    if i == 0 and st > 0:
        unpainted_sections.append((0, st))
    else:
        if painted_sections[i - 1][1] < st:
            unpainted_sections.append((painted_sections[i - 1][1], st))
        if i == n-1 and ed < l:
            unpainted_sections.append((ed, l))

if len(unpainted_sections)==0:
    print("All painted")
else:
    for (st, ed) in unpainted_sections:
        print(' '.join([str(st), str(ed)]))