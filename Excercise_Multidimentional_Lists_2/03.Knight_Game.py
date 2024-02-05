size=int(input())

matrix=[]
knight_moves=(
    (2,1),
    (2,-1),
    (-2,1),
    (-2,-1),
    (-1,2),
    (-1,-2),
    (1,2),
    (1,-2),
)
danger=False
removed=0
for i in range(size):
    matrix.append(list(input()))
while True:
    max_attacks=0
    coord=[]
    for i in range(size):
        for j in range(size):

            if matrix[i][j]=='K':
                current_attacks=0
                for x,y in knight_moves:

                    if 0<=i+x<size and 0<=j+y<size:

                        if matrix[i+x][j+y]=='K':
                            current_attacks+=1

                if current_attacks>max_attacks:
                    max_attacks=current_attacks
                    coord.append(x+i)
                    coord.append(j+y)
    if coord:
        matrix[coord[0]][coord[1]]='0'
        removed+=1
    else:
        break

print(removed)