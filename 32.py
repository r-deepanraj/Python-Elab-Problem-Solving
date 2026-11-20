num=int(input())
count=2
num_count=0
li=[]
for l in range(num):
    students=str(input()).lower()
    i=len(students)
    for j in range(0,i,2):
        b=students[j:j+count]
        li.append(b)
    print(li)
        # for k in range(len(li)):
        #     y=li[k]
        #     if y=="gb" or y=="bg":
        #         count +=1
        #         print(count)
        #     else:
        #         continue
        


# li=("a","b","c","c")
# count=0
# for i in range(len(li)):
#     val=(li[i])  
#     if val=="c" or "b":
#         count +=1
#     print(count)




        # for l in range(len(li)):
        #     if li=="gb" or "bg":
        #         num_count +=1
        # print(num_count)
        # num_count =num_count*0

