first,second=[int(x) for x in input().split()]
fset=set()
sset=set()
for _ in range(first):
    fset.add(int(input()))
for _ in range(second):
    sset.add(int(input()))
print(*(fset & sset),sep='\n')