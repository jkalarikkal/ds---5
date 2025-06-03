import matplotlib.pyplot as mat

x = [2,4,6,8,10]
y = [1,3,5,7,9]


mat.plot(x,y, 'r-', label = "Y == X", linewidth = 2)
mat.axis([0,5,0,10])
mat.xlabel("X-axis")
mat.ylabel("Y-axis")
mat.title("Sample graph")

mat.legend()
mat.show()

