num=int(input("ENTER  NUMBER : "))
temp=num
rev=0
while(num!=0):
    rev=rev*10+num%10
    num=num//10
  
print("THE REVERSE OF NUMBER ",temp,"IS",rev) 
if(rev==temp):
    print(temp,"IS PALINDROME")
else:
     print(temp,"IS NOT PALINDROME")
