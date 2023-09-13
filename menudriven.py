print("-----MENU DRIVEN CODE-----")
print("1:","ADDITION OF TWO NUMBERS")
print("2:","SUBTRACTION OF TWO NUMBERS")
print("3:","SUM OF FIVE DIGITS NUMBER  ")
ch=int(input("ENTER YOPUR CHOICE: "))

if(ch==1):
    a=int(input("enter first number:"))
    b=int(input("enter second number:"))
    c=a+b
    print("ADDITION OF TWO NUMBERS IS :",c)
elif(ch==2):
    d=int(input("enter first number:"))
    e=int(input("enter second number:"))
    f=d-e
    print("SUBTRACION OF TWO NUMBERS IS :",f)
elif(ch==3):
    n1=int(input("enter five digi number:"))
    sum=n1%10
    n1=n1//10
    sum=sum+n1%10
    n1=n1//10
    sum=sum+n1%10
    n1=n1//10
    sum=sum+n1%10
    n1=n1//10
    sum=sum+n1%10
    n1=n1//10
    sum=sum+n1%10
 
    print("SUM OF FIVE DIGITS NUMBER OF IS:",sum)
else:
    print("INVALID CHOICE")
print("----END OF MENU DRIVEN CODE-----")    

        
