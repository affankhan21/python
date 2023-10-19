from inheritvehicle import Vehicle
class Four(Vehicle):
    def __init__(self,vid=0,vname=None,vprice=0,vhtype=0,vmileage=0,vdoors=0):
        super().__init__(vid,vname,vprice)
        self.vhtype=vhtype
        self.vmileage=vmileage
        self.vdoors=vdoors
    def display(self):
        print("-------------------FOUR WHEELER-----------------------")
        super().display()
        print("VEHICLE  TYPE                 :",self.vhtype)
        print("VEHICLE  MILEAGE              :",self.vmileage)
        print("VEHICLE  DOOR NUMBER          :",self.vdoors)
        print("-------------------FOUR WHEELER END-----------------------")
#f1=Four(1234,"MERCEDES",3234535,"FOUR--WHEELER",10,4)
#f1.display()  