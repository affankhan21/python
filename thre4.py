import threading
import time

def display(stre):
    
    for s in stre:
        print(s,end=" ")
        time.sleep(2)

t1=threading.Thread(name="thread1",target = display,args=("good",))
t2=threading.Thread(name="thread2",target = display,args=("morning",))
t1.start()

t1.join()
t2.start()
t2.join()
print("I a m m a i n t h r e a d")


