#VARIABLE NUMBER OF ARGUMENTS
#def functionname(*arg)
#*arg indicates variable number of arguments

def sum(*arg):
    #OUPUT IS IN FORM OF TUPLE(,).
    sum1=0
    for i in arg:
        sum1=sum1+i
    print("SUM  =",sum1)


sum(10)   
sum(10,20)  
sum(10,20,30)   