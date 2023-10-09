num=int(input("ENTER THE NUMBER TO GET THE ADDITION :"))
a=num
sum1=0
while(num!=0):
    sum1=sum1+num%10
    num=num//10
print("THE SUM OF ",a,"IS",sum1)    


