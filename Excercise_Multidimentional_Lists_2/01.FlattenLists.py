n=input().split('|')
m=[x.split() for x in n]
[print(*m[len(m)-1-row], end=' ') for row in range(len(m))]