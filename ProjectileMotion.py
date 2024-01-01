import math
import matplotlib.pyplot as plot

from functions import *

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

angle = degreestoradians(angle)
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
        velocity = getVelo(xvelo, yvelo)
        accel = airconstant * velocity**2 / mass
        xvelo -= accel * (xvelo/velocity)*(0.01)
        yvelo -= accel * (yvelo/velocity)*(0.01)
        

print(xpositions)
print(ypositions)

plot.xlim(0, max(getRange(xpositions), getHeight(ypositions)) + 5)
plot.ylim(0, max(getRange(xpositions), getHeight(ypositions)) + 5)

plot.plot(xpositions,ypositions)

plot.title( "Range: " + str(int(getRange(xpositions))) + "          Max Height" + str(int(getHeight(ypositions))))

plot.show()




    
