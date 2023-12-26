import threading
import time



def display(sr):
    for i in sr:
        print(i,end="")
        time.sleep(3)

t1=threading.Thread(name="thread1",target=display,args=("Python",))
t2=threading.Thread(name="thread2",target=display,args=("For",))
t3=threading.Thread(name="thread3",target=display,args=("Everybody",))
t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()