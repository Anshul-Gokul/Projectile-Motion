import math
import matplotlib.pyplot as plot
import numpy

velocity = float(input("Input Velocity:"))
angle = float(input("Input Angle in Degrees:"))
height = float(input("Input Initial Height:"))
includeair = input("Include Air Resistance? (Y/N)")
if(includeair == 'Y'):
    air = True
else:
    False
if(air):
    airconstant = float(input("Input Air Resistance Constant"))
mass = float(input("Input Mass:"))

angle /= (180/math.pi)
xvelo = math.cos(angle) * velocity
yvelo = math.sin(angle) * velocity

xpositions = []
ypositions = []

currentyposition = height
currentxposition = 0

while(currentyposition > - 0.1):
    xpositions += [currentxposition]
    ypositions += [currentyposition]
    currentxposition += (0.01)*xvelo
    currentyposition += (0.01)*yvelo
    yvelo -= 0.01*(9.8)
    if(air):
        velocity = math.sqrt(xvelo**2 + yvelo**2)
        accel = airconstant * velocity**2 / mass
        xvelo -= accel * (xvelo/velocity)*(0.01)
        yvelo -= accel * (yvelo/velocity)*(0.01)
        

print(xpositions)
print(ypositions)

plot.xlim(0, xpositions[-1+len(xpositions)] + 5)
plot.ylim(0, xpositions[-1+len(xpositions)] + 5)

plot.plot(xpositions,ypositions)

plot.show()




    
