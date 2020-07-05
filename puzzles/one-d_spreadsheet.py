import sys
import math
from operator import add, sub, mul

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
cells = []
for i in range(n):
    operation, arg_1, arg_2 = input().split()
    cells.append([operation, arg_1, arg_2])

print(cells, file=sys.stderr)

operators = {"ADD": add, "SUB": sub, "MULT": mul}


def get_ref_cell_val(cell_num, ref_val):
    # print("Get ref cell val from cell {}=".format(cell_num), ref_val)
    ref_cell_num = int(ref_val.lstrip('$'))
    ref_cell_val = cells[ref_cell_num]
    # print("Ref cell val from cell {}=".format(cell_num), ref_cell_val)
    if type(ref_cell_val) is list:
        cells[ref_cell_num] = evaluate(ref_cell_num, ref_cell_val)
        # print(cells)
        return cells[ref_cell_num]
    else:
        return int(ref_cell_val)


def evaluate(cell_num, cell_val):
    # print('Evaluating {}='.format(cell_num), cell_val)
    # print('Get val_1 of {}'.format(cell_num), cell_val[1])
    val_1 = get_ref_cell_val(cell_num, cell_val[1]) if cell_val[1][0] == "$" else int(cell_val[1])
    # print('val_1 of {}='.format(cell_num), val_1)
    if cell_val[2] != '_':
        # print('Get val_2', cell_val[2])
        val_2 = get_ref_cell_val(cell_num, cell_val[2]) if cell_val[2][0] == "$" else int(cell_val[2])
        # print('val_2 of {}='.format(cell_num), val_2)

    if cell_val[0] == "VALUE":
        return int(val_1)
    else:
        return operators[cell_val[0]](val_1, val_2)


for i, val in enumerate(cells):
    if type(val) is list:
        # print('Evaluating cell {}'.format(i), val)
        cells[i] = evaluate(i, val)
    print("cell-{}".format(i),  cells[i])




