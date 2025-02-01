
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


# test
def g(x):
    return (x + 4) / 7 

# Parameters
p0 = 1.0  
TOL = 0.0001 
N0 = 100 

root = fixed_point_iteration(g, p0, TOL, N0)




