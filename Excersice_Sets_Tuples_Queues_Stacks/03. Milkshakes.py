from collections import deque

choco=[int(x) for x in input().split(', ')]
milk=deque(int(y) for y in input().split(', '))
shakes=0
while (choco and milk) and shakes<5:
    current_choco= choco.pop()
    if current_choco<=0:
        if choco:
            current_choco=choco.pop()
        else:
            continue
    current_milk=milk.popleft()
    if current_milk<=0:
        if milk:
            current_milk=milk.popleft()
        else:
            choco.append(current_choco)
            continue

    if current_milk==current_choco:
        shakes+=1

    else:
        choco.append(current_choco-5)
        milk.append(current_milk)

if shakes==5:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')

print(f"Chocolate: {', '.join([str(x) for x in choco]) if choco else 'empty'}")
print(f"Milk: {', '.join([str(x) for x in milk]) if milk else 'empty'}")