size=int(input())
matix=[]
sum=0
for i in range(size):
    matix.append([int(x) for x in input().split()])
for i in range(size):
    sum+=matix[i][i]
print(sum)