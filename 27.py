nums=int(input())


for i in range(1,nums+1):
    if i%2==0:
        current=2
    else:
        current=1
    for j in range(i):
        print(current,end=" ")
        current +=2
    print()