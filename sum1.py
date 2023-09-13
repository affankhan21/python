num=int(input("enter number:"))
sum=0
sum=sum+num%10
num=num//10
sum=sum+num%10
num=num//10
sum=sum+num%10
num=num//10

print("Addition of digits is:",sum)