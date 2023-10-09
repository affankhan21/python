#RECURSIVE FUNCTION FOR DISPLAYING SUM OF DIGITS OF A NUMBER 


def sumdigit(n):
    if(n==0):
        return 0
    else:
        return n%10+sumdigit(n//10)    










n=int(input("ENTER THE NUMBER FOR SUM OF DIGITS :"))
sumdigit(n)
print(sumdigit(n))