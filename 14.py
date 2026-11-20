month=int(input())
rent=float(input())
no_of_days=int(input())
percentage_of_rent=((20/100)*(rent))+rent
if month==4 or month==5:
    print(f"Rs.{percentage_of_rent*no_of_days}")
else:
    print(f"Rs.{rent*no_of_days:.2f}")