num=int(input())
val=2**num
change_str=str(val)
text_split=list(change_str)
convert_int=list(map(int, text_split))   
add=sum(convert_int)
print(convert_int)





num=int(input())
val=2**num
change_str=str(val)
total_sum=0
for item in change_str:
    total_sum+=int(item)
print(total_sum)