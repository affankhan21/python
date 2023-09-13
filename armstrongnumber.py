num=int(input("ENTER THE NUMBER TO CHECK ARMSTRONG: "))
dig=0
sum1=0
temp=num
temp1=temp

while(num!=0):
    num=num//10
    dig+=1
print("NUMBER OF DIGITS ARE :",dig) 
while(temp>0):
    sum1+=(temp%10)**dig
    temp=temp//10
 
if(temp1==sum1):
    print(temp1,"number is armstrong")
else:
    print(temp1,"number is not  armstrong")



