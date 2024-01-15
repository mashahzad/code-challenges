#Schrage's method for x10000

def randVal(seed):
    n = 1 # counter variable
    xN = seed #x0 = 1
    xNextn = 0

    # loop till we reach x10000
    while n<10001:
        xNextn = schrage(xN)
        xN = xNextn
        n=n+1
    print(xN)

# Schrage's method calculation of parameters for xN
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
    
    return xNew # return xN+1

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
    randVal(1)

