def sequence(opperation:str,x,y,num):
    if opperation=='Add':
        matrix[x][y]+=num
    if opperation=='Subtract':
        matrix[x][y] -= num

size=int(input())
matrix=[]

for i in range(size):
    matrix.append([int(x) for x in input().split()])

command=input().split()
while command[0]!="END":
    action,x,y,num=command
    x=int(x)
    y=int(y)
    num=int(num)
    if 0<=x<size and 0<=y<size:
        sequence(action,x,y,num)
    else:
        print(f"Invalid coordinates")

    command=input().split()

[print(*row) for row in matrix]
