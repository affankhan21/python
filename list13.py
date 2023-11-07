data15=[10,23,16,21,23,89,67,77,23]
# count method counts the number of specified element 
print(data15.count(23))
res=set(data15)
for x in res:
    print(x,data15.count(x))