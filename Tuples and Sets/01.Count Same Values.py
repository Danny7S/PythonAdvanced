num = tuple([float(x) for x in input().split()])
nums = []

for n in num:
    if n not in nums:
        rep = num.count(n)
        nums.append(n)
        print(f"{n} - {rep} times")
