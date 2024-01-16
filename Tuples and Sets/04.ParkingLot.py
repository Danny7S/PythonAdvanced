num_of_commands=int(input())
parking=set()
for _ in range(num_of_commands):
    command=input().split(', ')
    comm,car=command
    if (car not in parking) and (comm=='IN'):
        parking.add(car)
    elif (car in parking) and (comm=='OUT'):
        parking.remove(car)
if parking:
    for cars in parking:
        print(cars)
else:
    print('Parking Lot is Empty')