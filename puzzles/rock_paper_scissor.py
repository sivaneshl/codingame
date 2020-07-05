import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
ip = []
for i in range(n):
    numplayer, signplayer = input().split()
    # numplayer = int(numplayer)
    ip.append((numplayer, signplayer))


def match(p1, p2):
    # returns winner, loser
    p1_card, p2_card = p1[1], p2[1]
    if p1_card == p2_card:
        return (p1, p2) if int(p1[0]) < int(p2[0]) else (p2, p1)

    elif (
            (p1_card == 'C' and p2_card in ['P', 'L']) or
            (p1_card == 'L' and p2_card in ['P', 'S']) or
            (p1_card == 'S' and p2_card in ['R', 'C']) or
            (p1_card == 'P' and p2_card in ['R', 'S']) or
            (p1_card == 'R' and p2_card in ['C', 'L'])
    ):
        return p1, p2
    else:
        return p2, p1


def rounds(player_list):
    grps = zip(*(iter(player_list),)*2)
    winner_list = []
    for grp in grps:
        (winner, loser) = match(grp[0], grp[1])
        winner += (loser[0],)
        winner_list.append(winner)
    return winner_list[0] if len(winner_list) == 1 else rounds(winner_list)


winner = rounds(ip)
print(winner)
print(winner[0])
print(' '.join(list(winner[2:])))

