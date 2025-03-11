import matplotlib.pyplot as plt
def f(x):
    return x*x-4*x-10 

x=[]
y=[]
i=-6.0
while i<=6.0:
    x.append(i)
    y.append(f(i))
    i=i+0.25

    

plt.plot(x,y, color="red")
plt.grid()
plt.xlabel('X')
plt.ylabel('f(X)')
plt.title('Graph of f(x)')
plt.axhline(y=0,color="black")
plt.axvline(x=0,color="black")

plt.show()

x1=-2.0
x2=0

def bisection(x1,x2):
   for it in range(0,200):
       fx1=f(x1)
       fx2=f(x2)
       if(fx1*fx2>=0):
           print("No root found")
           break
       else :
           x0 = (x1+x2)/2
           fx0= f(x0)
           if(fx0==0):
               print("Root found")
               return x0
           else:
               if(fx1*fx0<0):
                   x2=x0
               else:
                   x1=x0
        
        
   return x0    
print(bisection(x1,x2))    