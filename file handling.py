try:
    fp=open("file1.txt","r")
    a=fp.read()
    print(a)
except FileNotFoundError:
    print("FILE NOT FOUND")
fp.close()    
