#FUNCTION WITH PARAMETERS AND WITH RETURN VALUE
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

num=int(input("ENTER THE NUMBER FOR FACTORIAL:"))
a=fact(num)    
print("THE FACTORIAL OF",num ,"IS",a)  