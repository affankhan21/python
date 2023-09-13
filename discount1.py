p=input("are u a student (y/n) :")
amt=float(input("enter the amount :"))
if(p=="y" or p=="Y"):
    if(amt>=2000):
        discount=amt*40/100
    else:
        discount=amt*8/100 
else:
    if(amt>=4000):
        discount=amt*25/100 
    else:
        discount=amt*3/100    

final=amt-discount
print("your total amount is: ",amt)
print("your discount is:",discount)
print("you pay :",final)         
