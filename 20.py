month=int(input())
days_31=[1,3,5,7,8,10,12]
days_30=[4,6,9,11]
if month in days_31:
    print("31 Days")
elif month in days_30:
    print("30 Days")
else:
    print("28/29 Days")