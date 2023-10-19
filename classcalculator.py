class Calculator:
    def getData(self):
        print("---------------------------------------------------------------------")
        self.num1=int(input("ENTER THE FIRST NUMBER :"))
        self.num2=int(input("ENTER THE SECOND NUMBER :"))
    def addition(self):
        return self.num1+self.num2
    def subtraction(self): 
        return self.num1-self.num2
    def multiplication(self): 
        return self.num1*self.num2  
    def division(self): 
        return self.num1/self.num2    
c=Calculator()
c.getData()
print("-----------RESULTS-----------------------------------------------------------")
print("ADDITION       :",c.addition())
print("SUBTRACTION    :",c.subtraction())
print("MULTIPLICATION :",c.multiplication())
print("DIVISION       :",c.division())
print("---------------------------------------------------------------------")
