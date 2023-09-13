amt=int(input("enter amount :"))
num=0
num1=num+amt//2000
amt=amt%2000
num2=num+amt//500
amt=amt%500
num3=num+amt//200
amt=amt%200
num4=num+amt//100
amt=amt%100
num5=num+amt//50
amt=amt%50
num6=num+amt//20
amt=amt%20
num7=num+amt//10
amt=amt%10
num8=num+amt//5
amt=amt%5

num9=num1+num2+num3+num4+num5+num6+num7+num8
print("2000",num1)
print("500",num2)
print("200",num3)
print("100",num4)
print("50",num5)
print("20",num6)
print("10",num7)
print("5",num8)
print("the minimum no of notes required are :",num9)