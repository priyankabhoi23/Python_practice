x,y=map(int,list(input("Enter the value of x and y:").split(" ")))
if x>0 and y>0:
    print(x," ",y," "," lies in first quadrant")
elif x<0 and y>0:
    print(x," ",y," "," lies in second quadrant")
elif x<0 and y<0:
    print(x," ",y," "," lies in third quadrant")
elif x>0 and y<0:
    print(x," ",y," "," lies in fourth quadrant")
elif x==0 and y==0:
    print(x," ",y," "," lies on origin")
elif x !=0 and y==0:
    print(x," ",y," "," lies on x-axis")
elif x ==0 and y!=0:
    print(x," ",y," "," lies on y-axis")
    
