principle=int(input("enter the principle:"))
rate=float(input("enter the rate:"))
t=int(input("enter the time:"))
amount=principle*((1+(rate/100))**t)
compound_interest=amount-principle
print(compound_interest)