amt=int(input("enter amount :"))
num=0
num=num+amt//2000
amt=amt%2000
num=num+amt//500
amt=amt%500
num=num+amt//200
amt=amt%200
num=num+amt//100
amt=amt%100
num=num+amt//50
amt=amt%50
num=num+amt//20
amt=amt%20
num=num+amt//10
amt=amt%10
num=num+amt//5
amt=amt%5




print("the minimum no of notes required are :",num)