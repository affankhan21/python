
try:
    a=int(input("ENTER NUMBER :"))
    b=int(input("ENTER NUMBER :"))
except ValueError:
    print("please enter only numbers")
else:
    c=a+b
    print(c)        