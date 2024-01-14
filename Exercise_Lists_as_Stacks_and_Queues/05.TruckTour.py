from collections import deque
num_of_stations=int(input())
statuions=deque()
tank=0
index=0
for _ in range(num_of_stations):
    current_station=[int(x) for x in input().split()]
    statuions.append(current_station)
copy_of_stations=statuions.copy()
while copy_of_stations:
    petrol,distance=copy_of_stations.popleft()
    tank+=petrol
    if tank>=distance:
        tank=tank-distance
    else:
        statuions.rotate(-1)
        copy_of_stations=statuions.copy()
        tank=0
        index+=1
print(index)




