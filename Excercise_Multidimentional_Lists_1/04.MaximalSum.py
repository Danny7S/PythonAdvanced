row, col=[int(x) for x in input().split()]

matrix=[]
check=(
    (1, 0),
    (1, 1),
    (0, 1),
)
max_sum=float('-inf')
biggest_matrix=[]
sum_of_matrix=0
for i in range(row):
    matrix.append([int(x) for x in input().split()])

for i in range(row-2):

    for j in range(col-2):
        sum_of_matrix=0
        for k in range(i,i+3):
            for m in range(j,j+3):
                sum_of_matrix+=matrix[k][m]

        if sum_of_matrix>max_sum:
            max_sum=sum_of_matrix
            biggest_matrix.clear()
            biggest_matrix.append(i)
            biggest_matrix.append(j)

print(f'Sum = {max_sum}')
r,c=biggest_matrix
print(*[matrix[r][c+x] for x in range(3)])
print(*[matrix[r+1][c+x] for x in range(3)])
print(*[matrix[r+2][c+x] for x in range(3)])