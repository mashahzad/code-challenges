#Schrage's method debug program with all details

def randVal(seed):
    a = 40014
    m = 2147483563
    q = 53668
    r = 12211
    xDivq = 0
    xModq = 0
    gX = 0
    n = 1
    print("Hello World!1")
    xN = seed
    xNextn = 0
    print("Hello World!2")
    while n<10001:
        print (xN)
        print("i am previous xN")
        xNextn = schrage(xN)
        xN = xNextn
        print (xN)
        print("i am updated xN")
        print (n)
        print("i am counter 'n'")
        n=n+1
        
def schrage(xNold):
    
    a = 40014
    m = 2147483563
    q = 53668
    r = 12211
    xDivq = 0
    xModq = 0
    gX = 0
    hX = 0
    xDivq = xNold // q
    axDivm = (a*xNold) // m 
    xModq = xNold % q
    gX = (a * xModq) - (r * xDivq)
    hX = xDivq - axDivm
    xNew = gX + m*hX
    
    return xNew

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
    randVal(1)