n=int(input())
biggest_interception=set()
for _ in range(n):
    first,second=input().split('-')

    start,end=[int(x) for x in first.split(',')]
    first_set=set(range(start,end+1))

    start, end = [int(x) for x in second.split(',')]
    second_set = set(range(start, end + 1))

    current_interception=first_set & second_set
    if len(biggest_interception)<=len(current_interception):
        biggest_interception=current_interception

print(f'Longest intersection is [{", ".join(map(str,biggest_interception))}] with length {len(biggest_interception)}')