try:
    fp=open("file1.txt","r")
    a=fp.read(15)
    print(a)
except FileNotFoundError:
    print("FILE NOT FOUND ")
fp.close()    