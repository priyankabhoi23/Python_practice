no=int(input("enter three digit no"))
n=no
temp=n%10
n=n//10
temp1=n%10
n=n//10
temp2=n
rev=(temp*100)+(temp1*10)+temp2

print(rev)
if rev==no:
    print("number is palindrome")
else:
    print("number is not palindrome")