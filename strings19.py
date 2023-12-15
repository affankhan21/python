data=input("ENTER STRING :")
temp="".join (set(data))
print(temp)
for ch in temp:
    print(ch,data.count(ch))
