num=int(input())

for i in range(num):
    val=str(input())
    val1=val[0]
    
    if val1.islower():
        print(str(val.lower()))
    else:
        print(str(val.upper()))