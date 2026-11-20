withdrawal_amount=int(input())
amount=float(input())
if withdrawal_amount<=amount:
    charge=(amount-0.5)-(withdrawal_amount)
    print(f"Current Balance : {charge:.2f}")
    print(f"Initial Balance : {amount:.2f}")
else:
    print("Invalid Withdrawal Request")
    print(f"Initial Balance : {amount:.2f}")