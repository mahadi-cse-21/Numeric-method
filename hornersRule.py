n = int(input("Enter power of x: "))
x = int(input("Enter a value for x: "))

func = []

for i in range(n + 1):
    func.append(int(input(f"Enter coefficient of x^{n-i}: ")))



sum = func[0]

for i in range(1, n + 1):
   
    sum = sum * x + func[i]

print(f"f(x) = {sum}")

"""
//input
5
3
5
4
3
2
-1
-7
// output
1628
"""