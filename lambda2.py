#USING LAMBDA FUNCTION FOR DISPLAY NUMBER IS POSITIVE  OR NOT

pos=lambda n:(n>0)
print(pos(10))
print(pos(-10))
a=int(input("ENTER NUMBER TO CHECK POSITIVE OR NOT:"))
print(pos(a))