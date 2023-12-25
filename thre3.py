import threading
import time

def display(stre):
    
    for s in stre:
        print(s,end=" ")
        time.sleep(2)

t1=threading.Thread(name="thread1",target = display,args=("hello",))
t2=threading.Thread(name="thread2",target = display,args=("world",))
t1.start()
t2.start()