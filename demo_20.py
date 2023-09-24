#PROGRAM  TO DEMONSTRATE IDENTITY OPERATOR
#WHEN ID IS SAME IS OPERATOR RETURNS  TRUE 
#WHEN ID IS DIFFERENT IS OPERATOR RETURNS  FALS+E 

x=10
y=20
print(x,id(x))
print(y,id(y))
print(x is y)
a=30
b=30
print(a,id(a))
print(b,id(b))
print(a is b)