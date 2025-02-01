
# Approximation Algorithm
x0 = 1.5
tol = 0.000001

iter = 0
diff = x0
x = x0

print(f"{iter} : {x}")

while diff >= tol:
    iter += 1
    y = x
    
    x = (x / 2) + (1 / x)
    
    print(f"{iter} : {x}")
    
    diff = abs(x - y)

print(f"\nConvergence after {iter} iterations")


# The Bisection Method
def bisection(f, a, b, tol, max_iter):
    i = 0  

    while abs(b - a) > tol and i < max_iter:
        i += 1
        p = (a + b) / 2  
        
        if (f(a) < 0 and f(p) > 0) or (f(a) > 0 and f(p) < 0):
            b = p  
        else:
            a = p  

    return p

def f(x):
    return x**2 - 2  

a = 0  
b = 3  
tol = 0.000001  
max_iter = 100  

root = bisection(f, a, b, tol, max_iter)
print(f"Approximated root: {root}")


# The fixed point iteration
def fixed_point_iteration(g, p0, TOL, N0):
    i = 1

    while i <= N0:
        p = g(p0)
        
        
        if abs(p - p0) < TOL:
            print(f"Approximated root: {p}")
            print("success")
            return p  
        p0 = p
        i += 1
    
   
    print("failure")
    return None  


# test
def g(x):
    return (x + 4) / 7 

# Parameters
p0 = 1.0  
TOL = 0.0001 
N0 = 100 

root = fixed_point_iteration(g, p0, TOL, N0)




# The Newton-Raphson method 

def newton_method(f, f_prime, pprev, TOL, N0):
    
    i = 1

    while i <= N0:
       
        if f_prime(pprev) != 0:
            
            pnext = pprev - f(pprev) / f_prime(pprev)

            if abs(pnext - pprev) < TOL:
                print(f"Approximated root: {pnext}")
                print("success")
                return pnext
            i+=1
            pprev = pnext  
        else:

            print("Unsuccessful: Derivative is zero.")
            return None

    print("Unsuccessful: Maximum iterations performed.")
    return None


# test
def f(x):
    return x**2 - 2  
def f_prime(x):
    return 2 * x  

pprev = 1.0 
TOL = 0.0001  
N0 = 100 

root = newton_method(f, f_prime, pprev, TOL, N0)



