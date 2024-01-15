num_of_std=int(input())
students=dict()

for _ in range(num_of_std):
    name, grade=input().split()
    grade=float(grade)
    if name not in students.keys():
        students[name]=[grade]
    else:
        students[name].append(grade)
for names, grades in students.items():
    avg=sum(grades)/len(grades)
    grades=[f'{x:.2f}' for x in grades ]
    print(f'{names} -> {" ".join(grades)} (avg: {avg:.2f})')