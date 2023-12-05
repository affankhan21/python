
try:
    a=int(input("ENTER NUMBER :"))
    b=int(input("ENTER NUMBER :"))
    c=a/b
except ValueError:
    print("please enter only numbers")
except ZeroDivisionError:
        print("number not divisible by zero")    
except:
    print("something went wrong")        
else:
    
    print(c)   