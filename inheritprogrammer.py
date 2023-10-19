from inheritemp import Employee
class Programmer(Employee):
    def __init__(self,eid=0,ename=None,basic=0,extrahrs=0,perhr=0):
        super().__init__(eid,ename,basic)
        self.extrahrs=extrahrs
        self.perhr=perhr
    def display(self):
        print("-----------PROGRAMMER-----------------------------------")
        super().display()    
        print("PROGRAMMER PER HOURS        :",self.perhr)
        print("PROGRAMMER EXTRA HOURS      :",self.extrahrs)
        print("-----------PROGRAMMER END--------------------------------")
#p1=Programmer(102,"RAHUL",34689,5,3456)
#p1.display()        


