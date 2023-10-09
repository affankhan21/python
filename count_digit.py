#FUNCTION WITH PARAMETER AND RETURN VALUE

def countdigits(num1):
    cnt=0
    while(num1!=0):
        num1=num1//10
        cnt=cnt+1
    return cnt
num=int(input("ENTER NUMBER TO COUNT:"))
b=countdigits(num)
print("THE COUNT OF ",num,"IS",b)

