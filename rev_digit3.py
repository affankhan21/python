# A PROGRAM TO CALCULATE REVERSE OF  A THREE DIGIT NUMBER


num=int(input("ENTER A TWO DIGIT NUMBER: "))
X=num
rev=0
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10

rev=rev*10+num%10
num=num//10
print("REVERSE OF TWO DIGIT NUMBER ",X,"IS",rev)
