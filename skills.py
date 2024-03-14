import math

def calcAreaOfRectangle(length, width):
    return length * width


def calcAreaOfSquare(lengthOfSide):
    return lengthOfSide*lengthOfSide


def calcAreaOfPentagon(lengthOfSide):
    temp = 5 * (5 + 2 * math.sqrt(5))
    squared = lengthOfSide * lengthOfSide
    return (1/4)*math.sqrt(temp)*squared


print(calcAreaOfRectangle(5,5))
print(calcAreaOfSquare(5))
print(calcAreaOfPentagon(5))