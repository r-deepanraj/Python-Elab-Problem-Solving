num=int(input())
val=1
n=[]
for i in range(1,num+1):
  val=i*val
val1=str(val)
print(val)
for j in range(len(val1)-1,-1,-1):
  n.append(int(val1[j]))
print(sum(n))
