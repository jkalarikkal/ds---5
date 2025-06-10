import matplotlib.pyplot as mat
import numpy as np


x = np.linspace(-10,10,1000)
m = int(input("What gradient: "))
c = int(input("What y intercept value: "))
y = (m*x) + c


#100 values between -5 and 5

mat.plot(x,y,'r--', label = f'y = {m}x + {c}')
mat.title('Plot of y = mx+c')
mat.xlabel('x')
mat.ylabel('y')
mat.legend()
mat.show()

print(x)