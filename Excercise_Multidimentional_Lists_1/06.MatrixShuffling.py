r,c=[int(x) for x in input().split()]

matrix=[]

for _ in range(r):
    matrix.append(input().split())

command=input().split()

while command[0]!='END':
    action,*cord=command
    cord=[int(x) for x in cord]
    if action!='swap' or len(cord)!=4 or not ((0<=cord[0] and cord[2]<r) and (0<=cord[1] and cord[3]<c)):
        print("Invalid input!")

    else:
        matrix[cord[0]][cord[1]], matrix[cord[2]][cord[3]] = matrix[cord[2]][cord[3]], matrix[cord[0]][cord[1]]
        [print(*row) for row in matrix]

    command=input().split()
