p1=int(input("enter price of first item:"))
p2=int(input("enter price of second item:"))
p3=int(input("enter price of third item:"))
p4=int(input("enter price of fourt item:"))
total=p1+p2+p3+p4
percentage=int(input("enter percentege of discount:"))
discount=total*percentage/100
final=total-discount
print("you have to pay:",final)
