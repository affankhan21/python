#FUNCTION WITHOUT PARAMETERS AND RETURN VALUE
def fact():
    num=int(input("ENTER THE NUMBER FOR FACTORIAL:"))
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

a=fact() 
print("THE FACTORIAL IS",a)   