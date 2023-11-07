data=[[31,10,2,30],[1,2,34,3,14],[110,22,33,444],[300,23,560,77]]
for  i in  data:
    print(i)
    #find the sum in a sublist
    max1=i[0]
    for x in i:
        if(max1<x):
            max1=x
    print(max1)    

