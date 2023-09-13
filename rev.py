num=int(input("enter number:"))
rev=0

rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10

print("reverse of 3 digit  is:",rev)