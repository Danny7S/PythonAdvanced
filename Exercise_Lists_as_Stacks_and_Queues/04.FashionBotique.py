racks=1
clothes=[int(x) for x in input().split()]
init_rack_cap=int(input())
rack_cap=init_rack_cap
while clothes:
    cloth = clothes.pop()
    if rack_cap>=cloth:
        rack_cap=rack_cap-cloth
    else:
        rack_cap=init_rack_cap
        racks=racks+1
        clothes.append(cloth)
print(racks)