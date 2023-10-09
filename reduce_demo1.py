import functools

sum1=lambda x,y:x+y

data=[2,4,53,56]
data1=[1,2,9,16,25,36,49,64,81]
print(functools.reduce(sum1,data))
print(functools.reduce(sum1,data1))