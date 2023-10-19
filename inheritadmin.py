from inheritemp import Employee
class Admin(Employee):
    def __init__(self,eid=0,ename=None,basic=0,target=0):
        super().__init__(eid,ename,basic)
        self.target=target
    def display(self):
        print("--------------ADMIN--------------------------")
        super().display()
        print("ADMIN TARGET                :",self.target)    
        print("--------------ADMIN- END--------------------------") 
#A1=Admin(105,"ARSHAN",74568,300)
#A1.display()        