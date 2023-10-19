class Vehicle:
    def __init__(self,vid=0,vname=None,vprice=0):
        self.vid=vid
        self.vname=vname
        self.vprice=vprice
    def display(self):
        print("VEHICLE  ID                   :",self.vid)
        print("VEHICLE  NAME                 :",self.vname)
        print("VEHICLE  PRICE                :",self.vprice)      
         
        

#v1=Vehicle(1,"WAGONR",78900)
#v1.display()      