import threading
import time
global lock
lock=threading.Lock()
class Account:
    def __init__(self,acno,name,balance):
        self.acno=acno
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        time.sleep(2)
        lock.acquire()
        self.balance=self.balance+amt
        lock.release()
    def withdraw(self,amt):
        if(self.balance>amt):
            time.sleep(2)
            lock.acquire()
            self.balance=self.balance-amt
            lock.release()        
        else:
            print("INSUFFICIENT BALANCE!!!")    
    def display(self):
        print("balance is:",self.balance)        