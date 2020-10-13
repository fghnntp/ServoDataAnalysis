from sympy import *
import matplotlib.pyplot as plt

x = Symbol('x')
f = (1/2)*x
f_1 = (-1/2)*x + 100
f1 = integrate(f, x)
f1_1 = integrate(f_1, x)
print(f1)
print(f1_1)
f2 = integrate(f1, x)
f2_2 = integrate(f1_1, x)
print(f2)
print(f2_2)
f_x = [i for i in range(200)]
f_y = [0.5*i for i in range(100)] + [(-0.5*i+100) for i in range(100,200)]
f1_x = [i for i in range(200)]
f1_y = [0.25*i**2 for i in range(100)] + [(-0.25*i**2+100*i) for i in range(100,200)]
f2_x = [i for i in range(200)]
f2_y = [0.0833*i**3 for i in range(100)] + [(-0.0833*i**3+50*i**2) for i in range(100,200)]

fig ,axs = plt.subplots(3)
axs[0].plot(f2_x, f2_y)
axs[1].plot(f1_x, f1_y)
axs[2].plot(f_x, f_y)

plt.show()

