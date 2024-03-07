n=int(input("enter 3 digit no: "))
temp1=n%10
n=n//10
temp2=n%10
n=n//10
temp3=n
rev=(temp1*100)+(temp2*10)+(temp3)
print("reverse",rev)