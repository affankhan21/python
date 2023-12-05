while(True):
    try:
        a=int(input("ENTER FIRST NUMBER   :"))
        if (a<0):
            a=-a
        b=int(input("ENTER SECOND NUMBER  :"))
        if(b<0):
            b=-b 
        c=a/b
        print("DIVISION ON OF ",a,"AND ",b,"IS",c)    
        break    
    except:
        print("please check b value it should not be 0")
    
   