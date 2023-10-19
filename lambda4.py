#USING LAMBDA FUNCTION FOR DISPLAY NUMBER IS ODD  OR NOT
odd=lambda n:(n%2!=0)
print(odd(10))
print(odd(-5))
a=int(input("ENTER NUMBER TO CHECK ODD OR NOT:"))
print(odd(a))