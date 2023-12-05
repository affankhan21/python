
def display():
    print("I am display method")
    print("Lets learn decorators")
def factorial(n):
    f = 1
    while n>=1:
        f=f*n
        n-=1
    return f
def finall(f1,f2):
    x=int(input("ENTER NUMBER FOR FACTORIAL:"))
    f1()
    print("FACTORIAL IS :",f2(x))  
finall(display,factorial)          