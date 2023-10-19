def DisplayRecord(**kwarg):
    for i,j in kwarg.items():
        print(i,"->",j,end=" ")
    print()    
    
DisplayRecord(bid=101,bname="LET US C",author="YASHWANT KANETKAR",price=345)
DisplayRecord(sid=102,sname="ABHISHEK",sperc=65,slocation="PUNE")
