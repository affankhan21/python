def sumdigit(n):
    if(n==0):
        return 0
    else:
        return n%10+ sumdigit(n//10)    


num=int(input("ENTER THE NUMBER  :"))

if(num<0):
    num=-(num)
else:
    num= num
a=sumdigit(num)    
print(a)