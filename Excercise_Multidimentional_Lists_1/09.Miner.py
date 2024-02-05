size=int(input())
command={
    'up':(-1,0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
field=[]
commands=input().split()
current_miner_cords=[]
collected_coal=0
avalable_coal=0

for row in range(size):
    field.append(input().split())
    avalable_coal+=field[row].count('c')

    if 's' in field[row]:
        current_miner_cords.append(row)
        current_miner_cords.append(field[row].index('s'))
field[current_miner_cords[0]][current_miner_cords[1]]= '*'

for com in commands:

    if 0<=command[com][0]+current_miner_cords[0]<size and 0<=command[com][1]+current_miner_cords[1]<size:
        current_miner_cords[0]= command[com][0] + current_miner_cords[0]
        current_miner_cords[1]= command[com][1] + current_miner_cords[1]

        if field[current_miner_cords[0]][current_miner_cords[1]]== 'c':
            field[current_miner_cords[1]][current_miner_cords[0]]='*'
            avalable_coal=avalable_coal-1

        if field[current_miner_cords[0]][current_miner_cords[1]]=='e':
            print(f"Game over! ({current_miner_cords[0]}, {current_miner_cords[1]})")
            break
    if avalable_coal == 0:
        print(f"You collected all coal! ({current_miner_cords[0]}, {current_miner_cords[1]})")
        break
else:
    print(f"{avalable_coal} pieces of coal left. ({current_miner_cords[0]}, {current_miner_cords[1]})")

