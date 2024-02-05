size=int(input())

matrix=[]
explode=(
    (1,0),
    (1,1),
    (1,-1),
    (0,1),
    (0,-1),
    (-1,0),
    (-1,1),
    (-1,-1),
)
alive_cells=0
sum=0
for row in range(size):
    matrix.append([int(x) for x in input().split()])

bombs=[tuple(int(y) for y in x.split(',')) for x in input().split()]

for x,y in bombs:
    if matrix[x][y]<=0:
        continue
    damage=matrix[x][y]
    matrix[x][y]=0

    for x_ex,y_ex in explode:

        if (0<=x+x_ex<size) and (0<=y+y_ex<size):

            if matrix[x+x_ex][y+y_ex]>0:
                matrix[x+x_ex][y+y_ex]-=damage

for row in range(size):
    for col in range(size):
        if matrix[row][col]>0:
            sum+=matrix[row][col]
            alive_cells+=1

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum}")
[print(*row) for row in matrix]
