start=int(input("ENTER THE START OF THE RANGE: "))
stop=int(input("ENTER THE STOP OF THE RANGE: "))
print("--------------------------------------------------------")
for i in range(start,stop+1,2):
    if(i%2==0):
        print(i," is a even number")
        
else:
    print("program finished") 
    print("--------------------------------------------------------")       