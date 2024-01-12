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
    tank=0
    for n in range(num_of_stations):
        current_station=copy_of_stations.popleft()
        if n==0:
            fill,_=current_station
            tank+=fill
        else:
            fill,distance=current_station
            if tank>=distance:
                tank=tank-distance
            else:
                index+=1
                statuions.rotate(-1)
                copy_of_stations = statuions.copy()
                break
            tank+=fill
print(index)




