num=int(input("ENTER THE NUMBER :"))
temp=num
rev=0
while(num!=0):
    rev=rev*10+num%10
    num=num//10
print("THE REVERSE OF ",temp,"IS",rev)    


