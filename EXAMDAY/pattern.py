n=int(input("enter row number: "))
def printpattern(a):
    for i in range (a,0,-1):
        for j in range(i,0,-1):
            print("*",end="")
        print()
           
printpattern(n)
        
