from collections import deque

materials=[int(x) for x in input().split()]
magic=deque(int(x) for x in input().split())
gifts={
    'Doll': [150,0],
    'Wooden train': [250,0],
    'Teddy bear':[300,0],
    'Bicycle': [400,0]

}
combo=False
while materials and magic:
    present=0
    current_material=materials.pop()
    current_magic=magic.popleft()

    present+=current_magic*current_material

    if present < 0:
        present=current_magic+current_material
        materials.append(materials)

    elif present==0:

        if current_magic==0 and current_material==0:
            continue

        elif current_material==0:
            magic.appendleft(current_magic)

        elif current_magic==0:
            materials.append(current_magic)

    else:
        increased=False
        for values in gifts.values():
            if present==values[0]:
                values[1]+=1
                increased=True

        if increased==False:
            current_material+=15
            materials.append(current_material)

if gifts['Teddy bear'][1]>=1 and gifts['Bicycle'][1]>=1:
    combo=True
elif gifts['Doll'][1]>=1 and gifts['Wooden train'][1]>=1:
    combo=True

if combo==True:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

for key,value in gifts.items():
    if value[1]>0:
        print(f'{key}: {value[1]}')