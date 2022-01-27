import math

def fermat(n):
    t0 = math.floor(math.sqrt(n))
    print("t0 = ", t0)
    square = False
    index = 1
    while square == False:
        t = t0 + index
        expr = math.pow(t,2) - n
        s = math.sqrt(expr)
        if math.floor(s) == s:
            square = True
            print("index = %d, t^2 - n = %d, n = t^2 - s^2 = %d^2 - %d^2, n = (t-s)(t+s) = %d * %d, yes" % (index, expr, t, s, t-s, t+s))
        else:
            print("index = %d, t^2 - n = %d, no" % (index, expr))
            index = index + 1

def f(x):
    return math.pow(x,2) + 1

def gcd(a,b):
    while(b):
        a, b = b, a % b
    return a

def pollard(x0, n):
    x = [x0]
    isDivisor = False
    index = 0
    while isDivisor == False:
        x.append(f(x[index]) % n)
        index = index + 1
        print("x[%d] = %d" % (index, x[index]))
        x.append(f(x[index]) % n)
        index = index + 1
        print("x[%d] = %d" % (index, x[index]))
        cmmdc = gcd(abs(x[index] - x[index//2]), n)
        print("gcd(abs(x[%d] - x[%d]),%d) = %d" % (index, index//2, n, cmmdc))
        if  cmmdc != 1:
            isDivisor = True
            print("n = %d * %d" % (cmmdc, n/cmmdc))

#pollard(2, 9599)
print(gcd(11,2520))