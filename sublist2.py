data=[[101,"AKSHAY",42000],[102,"BHAVANA",23000],[103,"SHWETA",31000],[104,"REEMA",15000]]

for i in range(1,len(data)):
    for j in range(0,len(data)-i):
        if data[j][2]>data[j+1][2]:
            data[j],data[j+1]=data[j+1],data[j]
print(data)        