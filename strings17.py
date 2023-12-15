data=input("ENTER STRING:").lower()

i=0
j=0
z=0
s=0
for k in data:
    if k in["a","e","i","o","u"]:
        i+=1
    elif k not in["a","e","i","o","u"]:
        j+=1
    elif k in[0,1,2,3,4,5,6,7,8,9]:
        z+=1    
    elif k not in["a","e","i","o","u"] and k in ["a","e","i","o","u"] and k  in[0,1,2,3,4,5,6,7,8,9]: 
        s+=1
print("vow",i)
print("con",j)
print("num",z)
print("spe",s)        