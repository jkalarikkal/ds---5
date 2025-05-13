import matplotlib.pyplot as mat

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

