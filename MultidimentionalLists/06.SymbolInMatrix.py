size=int(input())
matix=[]
found=False
for _ in range(size):
    matix.append([x for x in input()])
symboll=input()
for i in range(size):
    if found:
        break
    for j in range(size):
        if matix[i][j]==symboll:
            found=True
            break
if found:
    print(f'({i}, {j})')
else:
    print(f"{symboll} does not occur in the matrix")