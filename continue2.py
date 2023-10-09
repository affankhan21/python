for i in range(1,30):
    if(i%4==0):
        print(i,end=" ")
        if(i%6==0):
            print("6",end=" ")
        else:
            print("4",end=" ")
    elif(i%3==0):
        if(i%5==0):
            continue
        print(i,end=" ,")        

else:
    print("\nI AM DONE")    
