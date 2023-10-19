class Employee:
    def __init__(self,eid=0,ename=None,basic=0):
        self.eid=eid
        self.ename=ename
        self.basic=basic

    def display(self):
        print("-----------EMPLOYEE------------------------------")
        print("EMPLOYEE ID                 :",self.eid)
        print("EMPLOYEE NAME               :",self.ename)  
        print("EMPLOYEE BASIC              :",self.basic)  

#e1=Employee(101,"RAHUL",34500)
#e1.display()