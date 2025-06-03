import matplotlib.pyplot as mat
import numpy as np
'''
x = [2,4,6,8,10]
y = [1,3,5,7,9]

mat.plot(x,y)
mat.show()


mat.plot(x,y, 'ro')
mat.show()

mat.plot(x,y, 'g^')
mat.show()

mat.plot(x,y, 'r--')
mat.show()

mat.plot(x,y, 'b-')
mat.show()

mat.plot(x,y, 'b--')
mat.show()

mat.plot(x,y)
mat.axis([0,10,0,200])
mat.show()


mat.plot(x,y, 'r--', label = "Y == X", linewidth = 4)
mat.axis([0,10,0,50])
mat.xlabel("X-axis")
mat.ylabel("Y-axis")
mat.title("Sample graph")

mat.legend()
mat.show()


x = np.arange(0,10,0.2)

y1 = x**2
y2 = x**3

mat.plot(x,y1, 'r--', x, y2, 'b--')
mat.show()


x = np.linspace(-5,5,100)
m = 4
c = 15
y = (m*x) + c


#100 values between -5 and 5

mat.plot(x,y,'r--', label = f'y = {m}x + {c}')
mat.title('Plot of y = mx+c')
mat.xlabel('x')
mat.ylabel('y')
mat.legend()
mat.show()

print(x)


x = [5,9,4,2]
y = [13,18,11,6]

mat.bar(x,y, color = 'r')
mat.show()
'''

x1 = [1,3,5,7]
y1 = [2,4,6,8]
x2 = [2,4,6,8]
y2 = [1,2,3,4]

mat.bar(x1,y1, color = 'r')
mat.bar(x2, y2 , color = 'b')

mat.show()

mat.bar(["math", "english", "physics", "chemistry"], [67,39,87,94])
mat.show()


