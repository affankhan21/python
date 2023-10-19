class Time1:
    def getData(self):
        self.hr=int(input("ENTER HOUR :"))
        self.mn=int(input("ENTER MINUTES :"))
        self.sc=int(input("ENTER SECONDS :"))
    def DisplayData(self):
        print("THE ENTERED TIME IS ",self.hr,":",self.mn,":",self.sc)
t=Time1()
t.getData()
t.DisplayData()           