# val=int(input("num"))
# def func(*args):
#     return list(args[0])
# def disp():
#     for i in range(0,val+1):
#         for j in range(i):
#             print(values,end=" ")
#         print()

# values=func(input("23"))
# print(values)
# print(disp)



# # num=int(input())

# # def fun(*args):
# #     for i in range(0,num):
# #         for j in range(i):
# #             print(*args,end=" ")
# #         print()

# # values=fun(input())
# # print(values)


    
n = int(input())
l = []
for _ in range(n):
  l.append(input().strip())
  print(*l,end=" ")