import threading
import time

def display(stre):
    
    for s in stre:
        print(s,end=" ")
        time.sleep(2)

t1=threading.Thread(name="thread1",target = display,args=("hello",))
t2=threading.Thread(name="thread2",target = display,args=("everyone",))
t3=threading.Thread(name="thread2",target = display,args=("have a good day",))


t1.start()
t1.join()
print("good morning")
t2.start()
t2.join()
t3.start()
t3.join()