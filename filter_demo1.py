even=lambda n:n%2==0
odd=lambda  n:n%2!=0

data=[23,45,66,22,54,23,56,89]

print(list(filter(even,data)))

print(list(filter(odd,data)))