n=int(input("ENTER A NUMBER UPTO WHICH U WNAT SERIES:  "))
a=1
b=0
c=0
print(c,end=",")
for i in range(n):
    c=a+b
    print(c,end=", ")
    a=b
    b=c    

