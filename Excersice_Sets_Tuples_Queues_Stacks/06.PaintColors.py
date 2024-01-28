from collections import deque
from math import ceil
subs=deque(input().split())
main=deque()
while len(subs)>=2:
    front=subs.popleft()
    back=subs.pop()

    if front+back=='red' or front+back=='yellow' or front+back=='blue':
        main.append(front+back)

    elif back+front=='red' or back+front=='yellow' or back+front=='blue':
        main.append(back+front)

    elif front+back=='purple' or front+back=='green' or front+back=='orange':
        main.append(front+back)

    elif back+front=='purple' or back+front=='green' or back+front=='orange':
        main.append(back+front)

    else:
        front=front[:-1:]
        back=back[:-1:]
        if front!='':
            subs.insert(ceil(len(subs)/2),front)
        if back!='':
            subs.insert(ceil(len(subs)/2), back)
if subs:
    last_col=subs.pop()
    if last_col == 'red' or last_col == 'yellow' or last_col == 'blue':
        main.append(last_col)

    elif last_col == 'purple' or last_col == 'green' or last_col == 'orange':
        main.append(last_col)
if 'purple' in main and ('red' not in main or 'blue' not in main):
    main.remove('purple')

elif 'green' in main and ('yellow' not in main or 'blue' not in main):
    main.remove('green')

if 'orange' in main and ('red' not in main or 'yellow' not in main):
    main.remove('orange')
print([x for x in main])
