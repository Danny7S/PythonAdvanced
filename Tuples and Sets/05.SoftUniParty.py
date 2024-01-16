num_of_guests=int(input())
guests=set()
for _ in range(num_of_guests):
    guest=input()
    guests.add(guest)
command=input()
while command !='END':
    if command in guests:
        guests.remove(command)
    command=input()
print(len(guests))
if guests:
    guests=list(guests)
    guests.sort()
    for gg in guests:
        print(gg)




