mark1=int(input())
mark2=int(input())
mark3=int(input())
mark4=int(input())
mark5=int(input())
total_mark=((mark1+mark2+mark3+mark4+mark5)/5)

if total_mark>=90:
    print(f"{total_mark:.2f} Percent")
    print("Grade A")
elif total_mark>=80 and total_mark<90:
    print(f"{total_mark:.2f} Percent")
    print("Grade B")
elif total_mark>=70 and total_mark<80:
    print(f"{total_mark:.2f} Percent")
    print("Grade C")
elif total_mark>=60 and total_mark<70:
    print(f"{total_mark:.2f} Percent")
    print("Grade D")
elif total_mark>=40 and total_mark<60:
    print(f"{total_mark:.2f} Percent")
    print("Grade E")
else:
    print(f"{total_mark:.2f} Percent")
    print("Grade F")

