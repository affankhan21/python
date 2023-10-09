#1!+2!+3!+4!+5!......N!


def fact(num):
    f=1
    while(num!=0):
        f=f*num
        num=num-1
    return f  

def sum1(n):
    s=0   
    for i in range(1,n+1):
        s=s+fact(i)      
    return s

n=int(input("ENTER THE NUMBER :"))
a=sum1(n)
print("SUM OF SERIES IS :",a)    