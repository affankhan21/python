try:
    a=int(input("ENTER NUMBER :"))
    b=int(input("ENTER NUMBER :"))
    c=a/b
    print(c)  
except ValueError:
    print("please enter only numbers")
except ZeroDivisionError:
    print("enter divisor greater than zero") 
except:
    print("something went wrong")       
else:
   print("program end")       