num=int(input("ENTER  NUMBER TO REVERSE: "))
temp=num
rev=0
while(num!=0):
    rev=rev*10+num%10
    num=num//10
  
print("THE REVERSE OF NUMBER ",temp,"IS",rev)    