query_count=int(input())

nums=[]
for _ in range(query_count):
    query=input().split()
    if len(query)==2:
        _,num=query
        nums.append(num)
    elif query[0]=='2':
        if nums:
            nums.pop()
        else:
            continue
    elif query[0]=='3':
        if nums:
            print(max(nums))
        else:
            continue
    elif query[0]=='4':
        if nums:
            print(min(nums))
        else:
            continue
nums.reverse()
print(*nums, sep=', ')

