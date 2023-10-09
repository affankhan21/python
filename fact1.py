#FUNCTION WITHOUT PARAMETERS AND NO RETURN VALUE
def fact():
    num=int(input("ENTER THE NUMBER FOR FACTORIAL:"))
    f=1
    for i in range(1,num+1):
        f=f*i
    print("THE FACTORIAL OF ",num,"IS",f)

fact()    