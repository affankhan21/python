try:
    fp=open("file2.txt","w")
    fp.write("welcome to python \n")
    fp.write("welcome to world \n")
except FileNotFoundError:
    print("FILE NOT FOUND")
fp.close()   
fp=open("file2.txt","r")
a=fp.read(12)
print(a)
fp.close() 
