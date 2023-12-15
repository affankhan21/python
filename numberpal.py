num=int(input("ENTER NUMBER :"))
rev=0
temp=num
while(num!=0):
    rev=rev*10+num%10
    print(rev)
    num=num//10
    print(num)
if(rev==temp):
    print(temp,"ispal")
else:
    print(temp,"is not pal")
