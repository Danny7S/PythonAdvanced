size=int(input())

matrix=[]
primary_sum=0
secondary_sum=0

for i in range(size):
    matrix.append([int(x) for x in input().split()])
    secondary_sum += matrix[i][size-1-i]
    primary_sum += matrix[i][i]

print(abs(primary_sum-secondary_sum))