from collections import deque

robots = [x for x in input().split(';')]
robot_info = {}

for n in range(len(robots)):
    name, time = robots[n].split('-')
    robot_info[name] = int(time)

hours, minutes, seconds = map(int, input().split(':'))
command = input()
products = deque()
free_robots = []
rob = robot_info.copy()
free_robot = False

while command != 'End':
    products.append(command)
    command = input()

while products:
    seconds += 1

    if seconds > 59:
        seconds = 0
        minutes += 1

        if minutes > 59:
            minutes = 0
            hours += 1

    current_product = products.popleft()
    for name, time in rob.items():
        if time<robot_info[name]:
            rob[name]+=1
    for name, time in rob.items():
        if time == robot_info[name]:
            free_robot = True
            rob[name]=0
            break

    if free_robot:
        print(f'{name} - {current_product} [{hours:02d}:{minutes:02d}:{seconds:02d}]')
        free_robot = False
    else:
        products.append(current_product)
