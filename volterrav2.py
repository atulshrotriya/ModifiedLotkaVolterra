import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import integrate
alpha = 1. 
beta = 0.25 #mortality rate due to predators
delta = 1.
gamma = 1.
omega=1 #mortality rate due to humans
p=1 #human population factor
br=60 #birth rate of rabits per year
bf=6 #birth rate of foxes per year
x0 = 4.
y0 = 2.
dri=0.25 #initial mortality rate of rabbits based on lifespan in wild 2 yrs
drf=1 #initial mortality rate of foxes based on lifespan in wild 8 yrs
crf=0.0025 #crowding factor of rabbits based on 8 acre range)
cff=1 #crowding factor for foxes based on 3200 acre range
delr=1 #crowding effect based on family size 20
delf=0.15 #crowding effect based on pack size 3


def derivative(X, t, alpha, beta, delta, gamma):
    x, y = X
    dotx = br * x * (alpha - beta * y - omega * p - dri - crf * (x**delr))
    doty = bf * y * (-delta + gamma * x - drf - cff * (y**delf))
    return np.array([dotx, doty])
        
    

Nt = 1000
tmax = 30.
t = np.linspace(0.,tmax, Nt)
X0 = [x0, y0]
res = integrate.odeint(derivative, X0, t, args = (alpha, beta, delta, gamma))
x, y = res.T
plt.figure()
plt.grid()
plt.title("Population of Rabbits vs Foxes (human hunting rate = 1)")
plt.plot(t, x, '-', label = 'Rabbits')
plt.plot(t, y, '-', label = "Foxes")
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()

plt.show()

print ("The value of rabbits is: ", x[-1])
print ("The value of foxes is: ", y[-1])
