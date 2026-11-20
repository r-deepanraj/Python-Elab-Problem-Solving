num=int(input())
for i in range(1,num+1):
    for j in range(i):
        if i%2==0:
            print("fail",end=" ")
            
        else:
            print("pass",end=" ")
    print()