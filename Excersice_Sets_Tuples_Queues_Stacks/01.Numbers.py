first_s=set(int(x) for x in input().split())
second_s=set(int(x) for x in input().split())
com={
    'Add First': lambda x: first_s.update(int(num) for num in x),
    'Add Second': lambda x: second_s.update(int(num) for num in x),
    'Remove First': lambda x: first_s.difference_update(int(num) for num in x),
    'Remove Second': lambda x: second_s.difference_update(int(num) for num in x),
    'Check Subset': lambda x: print(first_s.issubset(second_s) or second_s.issubset(first_s))
}
num_of_comms=int(input())
for _ in range(num_of_comms):
    in_command, num_of_set,*data=input().split()
    command=in_command+' '+num_of_set
    com[command](data)
print(*first_s,sep=', ')
print(*second_s,sep=', ')