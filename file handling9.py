with open("file2.txt","a+")as fp:
   #print( fp.read())
   print(fp.tell())
  
   fp.write("python python  nextthing")
   print(fp.seek(0,0))
   print(fp.read())