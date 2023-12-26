import threading
import time
class mythread(threading.Thread):
    def __init__(self,data):
        super().__init__()
        self.data=data


def run(self):
   for sa in self.data:
        print(sa,end=" ")
        time.sleep(1)

t1=mythread("friday")
t1.start()
t2=mythread("python")
t2.start()            