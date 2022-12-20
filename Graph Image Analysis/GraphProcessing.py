import sys
from PIL import Image
import numpy as np
import math
np.set_printoptions(threshold=sys.maxsize)

# TODO
# 1. Instead of processing the line and making it a separate color,  
# treat it like whitespace.
# * Essentially, we want to get rid of the line detection and 
# the whitespace detection - keeping only the point detection
# ignoring all other pixels.


#returns a boolean value that determines if a pixel is considered whitespace.
def isWhitespace(pixel):
    return all([num > 250 for num in pixel])

# TODO
# 2. Make it so that the user can enter the color of the points on the graph
# Looking at the graphs, I have noticed that many have multiple colors.
# It might be helpful to make it so that the colors of the points are
# stored in an array -> if a pixel is any of the colors in the array, then add it to the point arr.
# This means that instead of having a function 'isBlackPixel', you should replace
# w/ a function 'pixelIsAPoint'.
# isBlackPixel(pixel: num[], pixelColors: num[][]): boolean
def pixelIsAPoint(pixel, pixelColors):
    pixel = [pixel[0], pixel[1], pixel[2]]
    for i in range (0, len(pixelColors)):
        curColor = pixelColors[i]
        if(pixelColorMatch(curColor, pixel)): return True
    return False

def pixelColorMatch(p1, p2):
    for i in range(0, len(p1)):
        if(math.abs(p1[i]-p2[i]) > 10):
            return False
    return True    

def createImageFunction(conditional, newVal):
    def newFunc(image):
        pixelArr = np.array(image)
        for line in pixelArr:
            for i in range(0, len(line)):
                if(conditional(line[i])):
                    line[i] = newVal
        return Image.fromarray(pixelArr)
    return newFunc

def processGraph(image, pointsClr, whitespaceClr, lineClr):
    colorGraphPoints = createImageFunction(isBlackPixel, pointsClr)
    filterWhitespace = createImageFunction(isWhitespace, whitespaceClr)
    def isLine(pixel):
        for i in range(0,len(pixel)):
            if(pixel[i] != pointsClr[i] and pixel[i] != whitespaceClr[i]):
                return True
        return False    
    processLines = createImageFunction(isLine, lineClr)
    return processLines(colorGraphPoints(filterWhitespace(image)))

def pixelIsColor(pixel, color):
    return np.array_equal(pixel, color)

# createAdjacentPointsArr(point: [num, num]): num[][] [[a,b],[c,d],[e,f]]
def createAdjacentPointsArr(point):
    resultArr = []
    for i in range(-1,2):
        for j in range(-1,2):
            resultArr.append([point[0]+i, point[1]+j])
    return resultArr

def detectPoints(image, pointsClr):
    # iterate through the image like we've been doing before.
    # we must create an array that stores where all the points are on the image.
    # when a new point is detected in the image, you push that new point onto the array.
    # -> How do we detect what is a point? If there is a pixel coord on the image where all of the 
    # adjacent pixels and the pixel itself is of pointsClr
    # Finally, return the array.
    colorLocationArr = []
    pointLocationArr = []
    pixelArr = np.asarray(image)
    for i in range(0, len(pixelArr)):
        for j in range(0, len(pixelArr[i])):
            if(pixelIsColor(pixelArr[i][j],pointsClr)):
                colorLocationArr.append([i,j])
    # for every point, check if all the points adjacent to that point are in the color location array.
    # If so, add that point to the pointLocationArr.
    for location in colorLocationArr:
        adjacentArr = createAdjacentPointsArr(location)
        if(all([pts in colorLocationArr for pts in adjacentArr])):
            pointLocationArr.append(location)
    return pointLocationArr