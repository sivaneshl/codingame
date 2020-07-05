import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# thor_tx: Thor's starting X position
# thor_ty: Thor's starting Y position
light_x, light_y, thor_x, thor_y = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    x_move, y_move = "", ""

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    if light_x > thor_x:
        thor_x += 1
        x_move = "E"
    elif light_x < thor_x:
        thor_x -= 1
        x_move = "W"

    if light_y > thor_y:
        thor_y += 1
        y_move = "S"
    elif light_y < thor_y:
        thor_y -= 1
        y_move = "N"

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(y_move + x_move)