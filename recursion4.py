#RECURSIVE FUNCTION FOR DISPLAYING FIBONACCI SERIES .
def fibo(n,a,b):
    if(n==0):
        return 1
    else:
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        return c+fibo(n-1,a,b)    







a=0
b=1

n=int(input("ENTER THE NUMBER :"))
print(a,b,end=" ")
fibo(n-2,a,b)