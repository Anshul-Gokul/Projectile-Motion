import math

def degreestoradians(x):
    return x/(180/math.pi)

def getVelo(xvelo, yvelo):
    magnitude = (xvelo**2 + yvelo**2)
    return math.sqrt(magnitude)

def getRange(position):
    return position[len(position) - 1]

def getHeight(positions):
    return max(positions)