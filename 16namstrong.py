no=int(input("enter the three digit no"))
n=no
temp=n%10
n=n//10
temp1=n%10
n=n//n
temp2=n
sum=(temp*temp*temp)+(temp2*temp2*temp2)+(temp1*temp1*temp1)
print(sum)
if no==sum:
    print("number is amstrong")
else:
    print("number is not amstrong")