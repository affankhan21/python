from inheritvehicle import Vehicle
class Two(Vehicle):
    def __init__(self,vid=0,vname=None,vprice=0,vhtype=0,vmileage=0):
        super().__init__(vid,vname,vprice)
        self.vhtype=vhtype
        self.vmileage=vmileage
    def display(self):
        print("-------------------TWO WHEELER-----------------------")
        super().display()
        print("VEHICLE  TYPE                 :",self.vhtype)
        print("VEHICLE  MILEAGE              :",self.vmileage)
        print("-------------------TWO WHEELER END-----------------------")
#t1=Two(123,"BULLET",234535,"TWO--WHEELER",30)
#t1.display()        
            
        
