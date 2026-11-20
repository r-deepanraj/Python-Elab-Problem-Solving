def func(*args):
    lis=str(*args)
    val=[]
    row_column=[]
    new_reverse=[]
    range_val=[]
    count=0
    values=0
    minus_values=-1
#list section
    for i in range(len(lis)):
        val.append(int(lis[i]))
    print(val)
#matrix sec

    for j in range(len(val)-1,1,-1):
        row_column.append(val[j])
    print(row_column)
#reverse matrix
    for k in range(len(row_column)-1,-1,-1):
        new_reverse.append(row_column[k])
    print(new_reverse)

#range
    for f in val:
        while 2>count:
            range_val.append(f)
            count +=1
    print(range_val)

#final

    for l in range(len(row_column)):
        if l !=0:
            va=row_column[values]+new_reverse[minus_values]
            values +=1
            minus_values -=1
            print(va)
            


    


       
        



val=func(int(input()))