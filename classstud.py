class Student:
    def getData(self):
        print("---------------------------------------------------------------------")
        self.id  =int(input        ("ENTER THE ID FOR STUDENT :"))
        self.name=input            ("ENTER THE NAME FOR STUDENT :")
        self.percentage=float(input("ENTER THE PERCENTAGE OF STUDENT :"))

    def DisplayData(self):
        print("STUDENT ID         :",self.id)    
        print("STUDENT NAME       :",self.name) 
        print("STUDENT PERCENTAGE :",self.percentage)
        print("---------------------------------------------------------------------") 
S1=Student()
S1.getData()
S1.DisplayData()