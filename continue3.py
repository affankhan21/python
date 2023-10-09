for i in range(1,30):
    if(i%3==0):
        print("3",end=" ")
        if(i%6==0):
            print("6",end=" ")
        
    elif(i%4==0):
        if(i%6==0):
            continue
        print("4",end=" ")        

else:
    print("\nI AM DONE")    
