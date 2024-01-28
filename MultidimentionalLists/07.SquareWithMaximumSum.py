row, col=[int(x) for x in input().split(', ')]
matrix=[]
sum=float('-inf')
for _ in range(row):
    matrix.append([int(x) for x in input().split(', ')])

for i in range(row-1):
    for j in range(col-1):
        curr_sum=matrix[i][j]+matrix[i+1][j]+matrix[i+1][j+1]+matrix[i][j+1]
        if curr_sum>sum:
            sum=curr_sum
            a=matrix[i][j]
            b=matrix[i+1][j]
            c=matrix[i + 1][j + 1]
            d=matrix[i][j + 1]
print(f'{a} {d}')
print(f'{b} {c}')
print(sum)