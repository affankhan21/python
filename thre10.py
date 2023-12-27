import threading
from thre_9 import Account
if  "__ name __== __main__":
    obj=Account(101,"yash",3000)
    t1=threading.Thread(name="thread1",target=obj.deposit,args=(2000,))
    t2=threading.Thread(name="thread2",target=obj.withdraw,args=(500,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    obj.display()