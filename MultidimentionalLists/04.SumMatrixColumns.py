row, col=[int(x) for x in input().split(', ')]
list=[]
for i in range(row):
    list.append([int(x) for x in input().split()])
for j in range(col):
    sum=0
    for k in range(row):
        sum=sum+list[k][j]
    print(sum)
