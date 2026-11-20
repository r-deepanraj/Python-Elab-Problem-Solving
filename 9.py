num=int(input())
tax=(18/100)*num
tip=(5/100)*num
print(f"The Tax is {tax}\nThe Tip is {tip:.2f}\nTotal Bill With Tax and Tip is {num+tax+tip:.2f}")