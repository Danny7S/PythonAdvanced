from collections import deque

parenT=deque([x for x in input()])
paren=parenT.copy()
balanced=True
while len(paren)>=2:
    current_parren=paren.popleft()
    next_paren=paren.popleft()
    if current_parren=='(':
        if next_paren==']' or next_paren=='}':
            balanced=False
            break
    elif current_parren=='{':
        if next_paren == ')' or next_paren==']':
            balanced = False
            break
    elif current_parren=='[':
        if next_paren == ')' or next_paren=='}':
            balanced = False
            break
    paren.appendleft(next_paren)
if balanced:

    print('YES')
else:
    print('NO')