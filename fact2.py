#FUNCTION WITH PARAMETERS AND NO RETURN VALUE
def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    print("THE FACTORIAL OF ",num,"IS",f)

num=int(input("ENTER THE NUMBER FOR FACTORIAL:"))
fact(num)    