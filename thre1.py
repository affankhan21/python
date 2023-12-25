import threading

def display():
    stre="Python Program"
    for s in stre:
        print(s,end=" ")

t1=threading.Thread(name="thread1",target = display)
t2=threading.Thread(name="thread2",target = display)
t1.start()
t2.start()