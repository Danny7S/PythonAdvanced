from collections import deque
from copy import deepcopy
r,c=[int(x) for x in input().split()]
string=input()

matrix=[]
start_string=deque(string)

for row in range(r):
    matrix.append([])
    for col in range(c):
        matrix[row].append(0)
print(matrix)
for row in range(r):

    for col in range(c):

        if len(start_string)==0:
            start_string.extend(string)

        if row%2==1:
                matrix[row][c-col-1]=start_string.popleft()
        else:
            matrix[row][col] = start_string.popleft()


[print(*row,sep='') for row in matrix]
