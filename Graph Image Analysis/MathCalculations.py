import sys
import numpy as np
import math
np.set_printoptions(threshold=sys.maxsize)

# return value is [E[X], E[Y], E[XY]]
# findMeanValue(pointsArr: nums[][]): nums[]
def findMeanValue(pointsArr):
    meanValue = [0,0,0]
    for point in pointsArr:
        meanValue[0] += point[0]
        meanValue[1] += point[1]
        meanValue[2] += point[0]*point[1]
    divideByLen = lambda elem : float(elem/len(pointsArr))
    return list(map(divideByLen, meanValue))

#E[XY]-E[X]E[Y]
# This just uses exactly the array that findMeanValue produces.
#findCovariance(meanValueArr: nums[]): num
def findCovariance(meanValueArr):
    return meanValueArr[2] - (meanValueArr[0]*meanValueArr[1])

# return value is [var[X], var[Y]]
# findVariance(pointsArr: nums[][]): nums[]
def findVariance(pointsArr, meanVal):
    varianceArr = [0,0]
    for point in pointsArr:
        varianceArr[0] += math.dist([meanVal[0]], [point[0]])
        varianceArr[1] += math.dist([meanVal[1]], [point[1]])
    return varianceArr

def findCorrelation(covariance, varianceX, varianceY):
    standardDeviationX = math.sqrt(varianceX)
    standardDeviationY = math.sqrt(varianceY)
    return float(covariance / (float(standardDeviationX * standardDeviationY)))

