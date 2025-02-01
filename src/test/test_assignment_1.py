
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


