str1=input("ENTER STRING TO REVERSE:")
rev=" "
i=len(str1)-1
while i>=0:
    rev+=str1[i]
    i-=1
print("ORIGINAL STRING IS :",str1)
print("REVERSE STRING IS  :",rev)    
