#FUNCTION WITH VARIABLE NUMBER OF KEYWORD ARGUMENTS
#kwarg-> KEYWORD ARGUMENT
#**->VARIABLE NUMBER OF KEYWORD ARGUMENTS
def DisplayRecord(**kwarg):
    for x,y in kwarg.items():
        print(x," -->",y,end="  ")
    print()    

DisplayRecord(bid=101,bname="THE LINUX PROGRAMMING INTERFACE",author="MICHAEL KERISK",PRICE=900)    
DisplayRecord(sid=102,name="MAHESH",PHONE=896897980,ADDRESS="PUNE")
DisplayRecord(Eid=103,Ename=" BHUSHAN KUMAR",salary=98604,ADDRESS="MUMBAI")