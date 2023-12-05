try:
    fp=open("file3.txt","a")
    fp.write("welcome to python \n")
    fp.write("welcome to world \n")
except FileNotFoundError:
    print("FILE NOT FOUND")
fp.close()   
