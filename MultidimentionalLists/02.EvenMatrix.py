rows=int(input())
list=[]
for _ in range(rows):
    list.append([int(y) for y in [int(x) for x in input().split(', ')] if y%2==0])
print(list)