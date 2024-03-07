name=input("enter the name")
roll_no=int(input("enter the roll no"))
c=float(input("enter the c marks "))
java=float(input("enter the java marks "))
python=float(input("enter the python marks "))


avg=c+java+python
per=avg/3
print("Name\tRoll\tc\tjava\tpython\tPercentage\t")
print(name,"\t",roll_no,"\t",c,"\t",java,"\t",python,"\t",per,"\t")
if per<35:
    print("Fail")
if per>=35:
    if per<50:
       print("Pass")
if per>=50:
    if per<70:
        print("second class")
if per>=70:
    if per<80:
        print("first class")
if per>=80:
    print("distinct")
