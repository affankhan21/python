#RECURSIVE FUNCTION FOR DISPLAYING SUM OF SERIES .


def sumseries(n):
    if(n==0):
        return 0
    else:
        return n+ sumseries(n-1)


n=int(input("ENTER NUMBER UPTO WHICH YOU WANT ADDITION :"))
sumseries(n)
print(sumseries(n))            