n = int(input("Enter the oroder of x: "))
x = int(input("Enter the value of x: "))

list = []
for i in range(n+1):
    list.append(int(input(f"Enter coefficient of x^{n-i}: ")))
result = 0
for i in range(n+1):
    result= result*x+list[i]
print((f"The result is of f(x) = {result}"))