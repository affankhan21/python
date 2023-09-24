#CALCULATE THE TOTAL PRICE BASED ON DISCOUNT OF 4ITEMS
i1=int(input("ENTER THE AMOUNT FOR FIRST ITEM : "))
i2=int(input("ENTER THE AMOUNT FOR SECOND ITEM : "))
i3=int(input("ENTER THE AMOUNT FOR THIRD ITEM : "))
i4=int(input("ENTER THE AMOUNT FOR FOURTH ITEM : "))
dis=int(input("ENTER DISCOUNT IN PERCENTAGE"))
amt=i1+i2+i3+i4
discount=amt*dis/100
finalamt=amt-discount
print("YOUR TOTAL AMOUNT IS :",amt,"RS")
print("YOUR DISCOUNT IS:",discount,"RS")
print("YOUR HAVE TO PAY  :",finalamt,"RS")