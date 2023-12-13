import datetime

d=int(input("ENTER DAY :"))
m=int(input("ENTER MONTH :"))
y=int(input("ENTER YEAR :"))
d1=datetime.datetime(y,m,d)
print(d1)
d2=(input("ENTER DATE (dd-mm-yyyy):"))
d2=d2.split("-")
d=int(d2[0])
m=int(d2[1])
y=int(d2[2])
d3=datetime.datetime(y,m,d)
print(d3)
diff=d3-d1
print(diff.days)