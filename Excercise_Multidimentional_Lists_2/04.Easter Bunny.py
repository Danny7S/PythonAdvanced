size = int(input())

field=[]
bunny=[]
final=[]
for i in range(size):
    field.append([int(el) if el.isnumeric() else el for el in input().split()])
    if 'B' in field[i]:
        bunny.append(i)
        bunny.append(field[i].index('B'))

max_sum=float('-inf')
directions=(
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
)

for i,j in directions:
    x=bunny[0]+i
    y=bunny[1]+j
    sum=0

    while 0<=x<size and 0<=y<size and field[x][y]!='X':

        if field[x][y]<=0:
            continue

        else:
            sum+=field[x][y]
        x = bunny[0] + i
        y = bunny[1] + j

    if sum>max_sum:
        max_sum=sum
        final.append(i)
        final.append(j)


x=bunny[0]+final[0]
y=bunny[1]+final[1]
while 0<=x<size and 0<=y<size and field[x][y]!='X':
    print(f'[{x}, {y}]')

print(max_sum)