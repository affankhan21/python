"""WE NEED TO CALCULATE THE PRICE OF FENCING RECTANGULAR FIELD 
    N TIMES """
length=float(input("ENTER THE LENGTH OF FIELD :"))
breadth=float(input("ENTER THE BREADTH OF FIELD :"))
peri=2*(length+breadth)
print("THE PERIMETER OF FIELD IS :",peri)
n=int(input("ENTER NUMBER OF TIMES :"))
totalarea=peri*n
price=float(input("ENTER THE PRICE FOR 1 METRE: "))
finlprice=totalarea*price
print("THE COST OF FENCING IS:",finlprice,"RS")