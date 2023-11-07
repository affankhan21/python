data=input("ENTER THE STRING :")
d=0
c=0
v=0
sp=0
i=0
for i in data:
    if i.isdigit():
        d+=1
    elif i in"aeiou":
        v+=1
    elif i.isalpha():
        c+=1
    else:
        sp+=1
print(len(data))        
print("vowels are :",v)
print("consonants are: ",c)
print("digits are : ",d)
print("special characters are :",sp)                    