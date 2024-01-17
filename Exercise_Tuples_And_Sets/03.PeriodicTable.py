n = int(input())
el = set()

for _ in range(n):
    el.update(x for x in input().split())

print(*el, sep='\n')