from inheritemp import Employee
class Sales(Employee):
    def __init__(self,eid=0,ename=None,basic=0,comission=0):
        super().__init__(eid,ename,basic)
        self.comission=comission
    def display(self):
        print("--------------SALES--------------------------")
        super().display()
        print("SALES COMISSION             :",self.comission)    
        print("--------------SALES END--------------------------") 
#S1=Sales(104,"AKBAR",45678,7000)
#S1.display()        