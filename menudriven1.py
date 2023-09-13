print("-----MENU DRIVEN CODE-----")

print("1:","CHECK WHETHER NUMBER IS PALINDROME NUMBER OR NOT")
print("2:","LOGIN VALIDATION  ")
print("3:","STUDENT DISCPUNT: ")
ch=int(input("ENTER YOPUR CHOICE: "))
       

if(ch==1):
    num=int(input("Enter number to check for palindrome:"))            
    rev=0
    temp=num
    rev=rev*10+num%10
    num=num//10
    rev=rev*10+num%10
    num=num//10
    rev=rev*10+num%10
    num=num//10
    if(rev==temp):
        print(temp,"is palindrome")
    else:
         print(temp,"is not palindrome")
elif(ch==2):

    import random
    user=input("enter username:")
    passw=input("enter password :")
    otp=random.randint(1000,9999)
    if(user=="abc")and(passw=="123"):
        utp=otp
        print("otp is :",utp)
        print("login succesful")
    else:
        print("login denied")
elif(ch==3):
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
else:
       print("INVALID CHOICE")
print("----END OF MENU DRIVEN CODE-----")                         
