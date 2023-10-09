for i in range(1,7):
    k=i
    for j in range(1,7):
        if(i==1)or(j==1)or(i==6)or(j==6):
            print("*",end=" ")
        else:       #for j in range(1,6):
            print(k,end=" ")
            k=k+1    
    print()    
