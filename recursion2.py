#RECURSIVE FUNCTION FOR DISPLAYING FACTORIAL OF A NUMBER 

def factorial(n):
    if(n==0):
        return 1
    else:
        return n * factorial(n-1)    






n=int(input("ENTER NUMBER FOR FACTORIAL :"))
factorial(n)
print(factorial(n))