# +ve -ve 0
n=int(input("enter the number:"))
if n>0:
    print("positive")
elif n==0:
    print("zero")
else:
    print("negative")

# odd even   
n=int(input("enter the number:"))
if n%2==0:
    print("even")
else:
    print("odd")
    
#greatest no btn 2 nos 
a=int(input("enter the 1st number:"))
b=int(input("enter the 2nd number:"))
if a>b:
    print("a is greater")
else:
    print("b is greater")
    
# eligibility for voting
a=int(input("enter the age:"))

if a>=18:
    print("can vote")
else:
    print("cannot vote")
    
# leap year or not
y=int(input("enter the year:"))

if y%4==0:
    print("leap")
else:
    print("not leap")
    
    
    