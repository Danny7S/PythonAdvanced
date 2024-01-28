import math
from collections import deque

bees=deque(int(x) for x in input().split())
nectar=[int(y) for y in input().split()]
symbols=deque(input().split())
honey=0
curr_honey=0
while bees and nectar and symbols:
    bee=bees.popleft()
    nect=nectar.pop()
    symbol=symbols.popleft()
    while bee>nect and nectar:
        nect=nectar.pop()

    if symbol=='-':
        curr_honey=abs(bee-nect)

    elif symbol=='+':
        curr_honey = abs(bee + nect)

    elif symbol=='*':
        curr_honey = abs(bee * nect)

    elif symbol=='/':
        if curr_honey==0:
            continue
        else:
            curr_honey=math.floor(abs(bee/curr_honey))

    honey+=curr_honey

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")
