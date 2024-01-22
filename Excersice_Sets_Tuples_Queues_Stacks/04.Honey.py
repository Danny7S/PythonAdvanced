import math
from collections import deque

bees=deque(int(x) for x in input().split())
nectar=[int(y) for y in input().split()]
symbols=[input().split()]
honey=0
curr_honey=0
while bees and nectar and symbols:
    bee=bees.popleft()
    nect=nectar.pop()
    symbol=symbols.pop()
    while bee>nect and nectar:
        bees.append(bee)
        nect=nectar.pop()

    if symbol=='-':
        curr_honey=abs(bee-nect)

    elif symbol=='+':
        curr_honey = bee + nect

    elif symbol=='*':
        curr_honey = bee * nect

    elif symbol=='/':
        if bee==0:
            continue
        curr_honey=math.floor(abs(bee/honey))
    honey+=curr_honey

print(f"Total honey made: {honey}")
print(f"Bees left: {', '.join([str(x) for x in bees])}")

