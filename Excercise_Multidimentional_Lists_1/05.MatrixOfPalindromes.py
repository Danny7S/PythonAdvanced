r,c=[int(x) for x in input().split()]

start=ord('a')

for first_last in range(start, start+r):

    for second in range(first_last,first_last+c):
        print(f'{chr(first_last)}{chr(second)}{chr(first_last)}', end=' ')

    print()
