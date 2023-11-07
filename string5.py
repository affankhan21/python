data1=input("ENTER THE STRING :")
temp="".join(set(data1))
print(temp)

for i in temp:
    print(i,data1.count(i))