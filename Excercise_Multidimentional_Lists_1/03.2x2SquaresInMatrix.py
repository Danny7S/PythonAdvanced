row, col=[int(x) for x in input().split()]

matrix=[]
check=(
    (1, 0),
    (1, 1),
    (0, 1),
)
similar=True
count=0

for i in range(row):
    matrix.append([x for x in input().split(' ')])

for i in range(row-1):

    for j in range(col-1):
        symbol=matrix[i][j]
        similar=True
        for x,y in check:
            current_symbol=matrix[i+x][j+y]

            if current_symbol!=symbol:
                similar=False
                break
        else:
            count+=1

print(count)
