import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

# The Theil-Sen Estimator is a way of finding the line of best fit.
# As opposed to normally finding the line of best fit, this one 
# is able to ignore outliers.

# "...the Theil–Sen estimator of a set of two-dimensional points (xi,yi) 
# is the median m of the slopes (yj − yi)/(xj − xi) determined by all 
# pairs of sample points. Sen (1968) extended this definition to handle
# the case in which two data points have the same x coordinate. 
# In Sen's definition, one takes the median of the slopes defined 
# only from pairs of points having distinct x coordinates"
# https://en.wikipedia.org/wiki/Theil%E2%80%93Sen_estimator
def findSlopeMedian(pointsArr: list[list[int]]) -> float:
    # going to have to loop through the pointsArr
    # in a nested loop in order to get every combination of slope.
    slopeArr = []
    for i in range(0, len(pointsArr)):
        curPoint = pointsArr[i] # [x,y]
        for j in range(i+1, len(pointsArr)): # i+1 since we don't want repeat slope calculations. (order does not matter)  
            if (pointsArr[j][0] != curPoint[0]): # add if the x values are not the same.
                slope = float((pointsArr[j][1] - curPoint[1]) / (pointsArr[j][0] - curPoint[0]))
                slopeArr.append(slope)
    # Now we have an array of all of the slopes. We must determine the median.
    slopeArr.sort() # O(n^2)log(n^2) since the slopeArr is of length n^2 ((n/2)*n) to be precise.
    return np.median(slopeArr)
# "Once the slope m has been determined, 
# one may determine a line from the sample points 
# by setting the y-intercept b to be the median of the values yi − mxi"
# https://en.wikipedia.org/wiki/Theil%E2%80%93Sen_estimator
def findIntercept(pointsArr: list[list[int]], slope: float) -> float:
    interceptArr = []
    for point in pointsArr:
        interceptArr.append(float(point[1] - (slope * point[0])))
    interceptArr.sort()
    return np.median(interceptArr)

# returns the line of best fit in the format [slope, intercept]
def getLine(pointsArr: list[list[int]]) -> list[float]:
    slope = findSlopeMedian(pointsArr)
    return [slope, findIntercept(pointsArr, slope)]
    
