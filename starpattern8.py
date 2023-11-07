

"""
OUTPUT:
* * * * * * 
* 2 3 4 5 * 
* 3 4 5 6 * 
* 4 5 6 7 * 
* 5 6 7 8 * 
* * * * * * 
"""








for i in range(1,7):
    k=i
    for j in range(1,7):
        if(i==1)or(i==6)or(j==1)or(j==6):
            print("*",end=" ")
        else:
            print(k,end=" ")  
            k=k+1
    print()            
  