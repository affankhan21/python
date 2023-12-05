try:
    
    a=int(input("ENTER NUMBER :"))
    b=int(input("ENTER NUMBER :"))
    try:
        c=a/b
        print(c) 
    except ZeroDivisionError:
        print("number not divisible by zero")
except ValueError:
    print('ONLY NUMERIC VALUE')
except:
    print("something went wrong")
else:
   print("program end")                   