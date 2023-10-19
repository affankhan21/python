class Employee:
    def __init__(self,id=101,name="RAHIL",department="FINANCE",salary=34567):
        self.id=id
        self.name=name
        self.department=department
        self.salary=salary
    def DisplayData(self):
        print("EMPLLOYEE ID          :",self.id)
        print("EMPLOYEE  NAME        :",self.name)
        print("EMPLOYEE DEPARTMENT   :",self.department)
        print("EMPLOYEE SALARY       :",self.salary)
e1=Employee()
e1.DisplayData()   
e2=Employee(102,"RAJ","HR",8900)
e2.DisplayData()   