def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)    


num=int(input("ENTER THE NUMBER :"))

if(num<0):
    num=-(num)
else:
    num= num
a=fact(num)    
print(a)