def funct(x):
    return x * x - 3 * x + 2

def fun(x):
    return 2 * x - 3

x0 = 0.0

for i in range(200):
    x1 = x0 - funct(x0) / fun(x0)
    if abs(x1 - x0) < 0.000000001:
        print(f"Root found: {x1}")
        break
    x0 = x1
else:
    print("Maximum iterations reached without convergence.")
