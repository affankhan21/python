# A PROGRAM TO CALCULATE SUM OF THREE  DIGIT NUMBER


num=int(input("ENTER A TWO DIGIT NUMBER: "))
X=num
sum1=0
sum1=sum1+num%10
num=num//10
sum1=sum1+num%10
num=num//10
sum1=sum1+num%10
num=num//10

print("SUM OF TWO DIGIT NUMBER ",X,"IS",sum1)
