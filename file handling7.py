with open("file1.txt","rb") as fp:
   print(fp.seek(40,0))
   print(fp.read())
   print(fp.tell())
   print(fp.seek(-5,2))
   print(fp.read())
   print(fp.tell())
   print(fp.seek(3,1))
   print(fp.read())
   print(fp.tell())

