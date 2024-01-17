n=int(input())
odd=set()
even=set()
for row in range(n):
    sum_of_name=int(sum((ord(x) for x in input()))/(row+1))
    if sum_of_name%2==0:
        even.add(sum_of_name)
    else:
        odd.add(sum_of_name)
if sum(odd)==sum(even):
    print(*(odd & even), sep=', ')
elif sum(odd)>sum(even):
    print(*(odd - even), sep=', ')
elif sum(odd)<sum(even):
    print(*(odd.symmetric_difference(even)), sep=', ')
