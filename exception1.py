while(True):
    try:
        a=int(input("ENTER FIRST NUMBER   :"))
        if (a<0):
            a=-a
        b=int(input("ENTER SECOND NUMBER  :"))
        if(b<0):
            b=-b 
    except:
        print("PLEASE ENTER NUMERICAL VALUE ")
    else:
        c=a-b
        print("SUBTRACTION OF ",a,"AND ",b,"IS",c)    
        break