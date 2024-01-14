from collections import deque

parenT=deque([x for x in input()])
opened=['(','[','{']
balanced=True
open_p=deque()
while parenT:
    current_parren=parenT.popleft()
    if current_parren in opened:
        open_p.append(current_parren)
    else:
        if open_p:
            previous_parren=open_p.pop()
            if (previous_parren == '(') and (current_parren == ')') or \
                    (previous_parren== '{') and (current_parren == '}') or \
                    (previous_parren == '[') and (current_parren == ']'):
                continue
            else:
                balanced=False
                break
if balanced:
    print('YES')
else:
    print('NO')


