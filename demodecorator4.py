def display():
    print("in display")
def newf(f1):
    def newf2():
        print("f2 started")
        f1()
        print("f2 end")    
    return newf2
r=newf(display) 
r()   
print(r)