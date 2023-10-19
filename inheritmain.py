from inheritemp import Employee
from inheritprogrammer import Programmer
from inheritadmin import Admin
from inheritsales import Sales


S1=Sales(104,"AKBAR",45678,7000)
p1=Programmer(102,"RAHUL",34689,5,3456)
A1=Admin(105,"ARSHAN",74568,300)

data=[S1,p1,A1]
for i in data:
    i.display()
        