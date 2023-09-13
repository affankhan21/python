import random
user=input("enter username:")
passw=input("enter password:")
otp=random.randint(1000,9999)
if(user=="abc")and(passw=="123"):
    utp=otp
    print("otp is :",utp)
    print("login succesful")
else:
    print("login denied")    
