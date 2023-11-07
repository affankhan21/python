data1=input("enter string for palindrome :")
i=0
j=len(data1)-1
while i >= 1:
    if data1[i]==data1[j]:
        i+=1
        j-=1
    else:
        print(" not palindrome")
        break
else:
    print("palindrome")               