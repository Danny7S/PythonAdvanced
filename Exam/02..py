size=int(input())

armour=300
enemies=0
jet=[]
field=[]
for i in range(size):
    field.append([x for x in input()])

    if 'J' in field[i]:
        jet.extend([i,field[i].index('J')])
        field[jet[0]][jet[1]]='-'

    if 'E' in field[i]:
        enemies+=field[i].count('E')
neutralized=False
moves={
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1)
}

while armour>0:

    if enemies==0:
        neutralized=True
        break

    command = input()
    x=moves[command][0]
    y=moves[command][1]
    jet[0]+=x
    jet[1]+=y
    if field[jet[0]][jet[1]]=='-':
        continue

    elif field[jet[0]][jet[1]]=='R':
        armour=300
        field[jet[0]][jet[1]]='-'

    elif field[jet[0]][jet[1]]=='E':

        if armour>100:
            armour-=100
            field[jet[0]][jet[1]]='-'
            enemies-=1

        else:
            if enemies==1:
                neutralized=True
                break
            else:
                armour-=100
field[jet[0]][jet[1]]='J'
if neutralized==True:
    print('Mission accomplished, you neutralized the aerial threat!')

else:
    print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet[0]}, {jet[1]}]!")

[print(*row,sep='') for row in field]