from collections import deque

money=[int(x) for x in input().split()]
food=deque([int(x) for x in input().split()])

items_bought=0
while money and food:
    current_amount=money.pop()
    price=food.popleft()

    if price>current_amount:
        continue

    elif price==current_amount:
        items_bought+=1

    else:
        items_bought += 1
        change=current_amount-price

        if money:
            money[-1]+=change

if items_bought>=4:
    print(f"Gluttony of the day! Henry ate {items_bought} foods.")

elif items_bought==0:
    print("Henry remained hungry. He will try next weekend again.")
elif items_bought==1:
    print(f"Henry ate: {items_bought} food.")
else:
    print(f"Henry ate: {items_bought} foods.")

