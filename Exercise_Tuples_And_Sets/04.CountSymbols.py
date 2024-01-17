n=input()
set=set(x for x in n)
for letter in sorted(set):
    print(f'{letter}: {n.count(letter)} time/s')