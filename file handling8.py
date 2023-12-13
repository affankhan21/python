with open("file2.txt","w+")as fp:
   #print( fp.read())
   print(fp.tell())
  
   fp.write("python is language !python is the next big thing")
   print(fp.seek(0,0))
   print(fp.read())