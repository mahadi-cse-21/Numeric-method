def funct(x):
    return x * x - 3 * x + 2

x0 = 0.0
x1 = 1.0

for i in range(200):
    if funct(x1) - funct(x0) == 0:
        print("Division by zero error!")
        break
    x2 = x1 - funct(x1) * (x1 - x0) / (funct(x1) - funct(x0))
    
    if abs(x2 - x1) < 0.000001:
        print(f"Root found: {x2}")
        break
    
    x0 = x1
    x1 = x2
else:
    print("Maximum iterations reached without convergence.")
