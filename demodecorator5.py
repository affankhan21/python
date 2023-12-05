def newf(f1):
    def newf2():
        print("f2 started")
        f1()
        print("f2 end")    
    return newf2

@ newf
def display():
    print("in display")

display()