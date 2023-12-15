data=input("ENTER STRING:")
i=0
l=len(data)-1
while(i<l):
    if(data[i]==data[l]):
       
        i+=1
        l-=1
    else:
        print("not palindrome")
        break
else:
    print(data," is palindrome")
