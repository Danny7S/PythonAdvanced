size=int(input())

matrix=[]
sum_primary=0
sum_secondary=0

for i in range(size):
    matrix.append([int(x) for x in input().split(', ')])
    sum_primary+=matrix[i][i]
    sum_secondary+=matrix[i][size-1-i]

print(f"Primary diagonal: {', '.join([str(matrix[i][i]) for i in range(size)])}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join([str(matrix[i][size-1-i]) for i in range(size)])}. Sum: {sum_secondary}")