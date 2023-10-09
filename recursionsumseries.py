def sumseries(n):
    if(n==0):
        return 0
    else:
        return n + sumseries(n-1)    



num=int(input("ENTER THE NUMBER UPTO WHICH YOU WANT ADDITION OF SERIES :"))

if(num<0):
    num=-(num)
else:
    num= num
a=sumseries(num)    
print(a)