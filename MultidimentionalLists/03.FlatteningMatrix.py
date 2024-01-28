rows=int(input())
list=[]
for _ in range(rows):
    list.extend([int(x) for x in input().split(', ')])
print(list)