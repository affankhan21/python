pos=lambda n:n>=0
neg=lambda  n:n<0

data=[89,-56,45,-78,45,90,-90,45]

print(list(filter(pos,data)))

print(list(filter(neg,data)))