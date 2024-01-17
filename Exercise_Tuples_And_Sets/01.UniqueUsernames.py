num_of_names=int(input())
names=set()
for _ in range(num_of_names):
    names.add(input())
print(*names, sep='\n')