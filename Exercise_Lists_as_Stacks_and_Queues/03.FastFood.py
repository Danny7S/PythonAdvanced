from collections import deque
food=int(input())
orders=deque([int(x) for x in input().split()])
print(max(orders))
while orders:
    current_order=orders.popleft()
    if current_order<=food:
        food=food-current_order
    else:
        orders.appendleft(current_order)
        break
if orders:
    print(f"Orders left: {' '.join(map(str,orders))}")
else:
    print('Orders complete')