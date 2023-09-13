len=float(input("enter length of field:"))
brea=float(input("enter breath of field:"))
perimeter=2*(len+brea)
num=int(input("how many times to wire:"))
cost=float(input("cost of wire :"))
totalcost=cost*num*perimeter
print(totalcost)