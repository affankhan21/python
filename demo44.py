#FUNCTION SHOWING THE USE OF DEFAULT ARGUMENTS

def sum(x=0,y=0,z=0):
    a=x+y+z
    return a          
res=sum(10,20,30)
print("RESULT OF (10,20,30) IS :",res)
res=sum(10,20)
print("RESULT OF (10,20) IS :",res)
res=sum(10)
print("RESULT OF (10) IS :",res)
res=sum()
print("RESULT OF () IS :",res)