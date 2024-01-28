row,col=input().split(', ')
row=int(row)
summ=0
list=[]
for _ in range(row):
    nums=[int(x) for x in input().split(', ')]
    summ+=sum(nums)
    list.append(nums)
print(summ)
print(list)