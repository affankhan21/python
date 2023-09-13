num=int(input("ENTER THE NUMBER : "))
sum2=0
temp=num
while(num>0):
    sum2=sum2+num%10
    num=num//10
print("SUM OF ",temp,"IS",sum2)   