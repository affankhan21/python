from inheritvehicle import Vehicle
from inherittwo import Two
from inheritfour import Four


t1=Two(13,"BULLET",234535,"TWO--WHEELER",30)
f1=Four(1234,"MERCEDES",3234535,"FOUR--WHEELER",10,4)
    

data=[t1,f1]
for i in data:
    i.display()
        