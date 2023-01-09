import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

def downScaleImage(image: Image) -> Image:
    sizeArr = image.size
    while(sizeArr[0]*sizeArr[1] > 50000):
        sizeArr = list(map(lambda x : math.floor(x/5), sizeArr))
    lowResImage = image.resize(sizeArr, Image.ANTIALIAS)
    return lowResImage

def pixelIsAPoint(pixel: list[int], pixelColors: list[list[int]]) -> bool:
    pixel = [pixel[0], pixel[1], pixel[2]]
    for i in range (0, len(pixelColors)):
        curColor = pixelColors[i]
        if(pixelColorMatch(curColor, pixel)): return True
    return False

def pixelColorMatch(p1: list[int], p2: list[int]) -> bool:
    for i in range(0, len(p1)):
        if(abs(p1[i]-p2[i]) > 10): return False
    return True    

def createPoints(image: Image, pointsClr: list[list[int]], pointSize: int) -> list[list[list[int]]]:
    pixelArr = np.asarray(image)
    imgHeight = image.size[1]
    coordinateArr = []
    visitedCoords = set()
    for i in range(0, len(pixelArr)): 
        for j in range(0, len(pixelArr[i])): 
            if(pixelIsAPoint(pixelArr[i][j],pointsClr) and not (tuple([i,j]) in visitedCoords)):
                coordinateArr = dfsCreatePoints(pixelArr, [i, j], visitedCoords, pointsClr, pointSize, coordinateArr, imgHeight)
    return coordinateArr 

def dfsCreatePoints(pixelArr: list[list[int]], startingCoord: list[int], visitedCoords: set[tuple[int]], pointsClr: list[list[int]], pointSize: int, coordinateArr: list[list[int]], imgHeight: int) -> list[list[int]]:
    stack = [tuple(startingCoord)]
    pixelCounter = 0
    while(len(stack) != 0):
        curCoord = stack.pop()
        if(curCoord not in visitedCoords and (pixelIsAPoint(pixelArr[curCoord[0]][curCoord[1]], pointsClr))):
            pixelCounter += 1
            visitedCoords.add(curCoord)
            stack = appendAdjacentPoints(stack, curCoord, pixelArr)
            if(pixelCounter >= pointSize):
                pixelCounter = 0
                coordinateArr.append([curCoord[1], imgHeight - curCoord[0]])
    return coordinateArr


def pointSize(image: Image, pointsClr: list[list[int]]) -> int:
    pixelArr = np.asarray(image)
    pointSizes = []
    visitedCoords = set() 
    for i in range(0, len(pixelArr)): 
        for j in range(0, len(pixelArr[i])): 
            if(pixelIsAPoint(pixelArr[i][j],pointsClr) and not (tuple([i,j]) in visitedCoords)):
                pointSizes.append(dfsPointSize(pixelArr, [i,j], visitedCoords, pointsClr))
    return mode(pointSizes)

def mode(arr: list[int]) -> int:
    frequencyMap = {}
    for val in arr:
        if(val in frequencyMap):
            frequencyMap[val] += 1
        else:
            frequencyMap[val] = 1
    maxFrequencyArr = []
    curMax = 0
    for key, value in frequencyMap.items():
        if(value == curMax):
            maxFrequencyArr.append(key)
        if(value > curMax):
            maxFrequencyArr = [key]
            curMax = value
    maxFrequencyArr.sort()
    return maxFrequencyArr[0] # return the smallest number if there is a tie.

def dfsPointSize(pixelArr: list[list[int]], startingCoord: list[int], visitedCoords: set[tuple[int]], pointsClr: list[list[int]]) -> int:
    stack = [tuple(startingCoord)]
    islandSize = 0
    while(len(stack) != 0):
        curCoord = stack.pop()
        if(curCoord not in visitedCoords and (pixelIsAPoint(pixelArr[curCoord[0]][curCoord[1]], pointsClr))):
            islandSize += 1
            visitedCoords.add(curCoord)
            stack = appendAdjacentPoints(stack, curCoord, pixelArr)
    return islandSize

# adds only those adjacent pixels that are within the bounds of the pixelArr.
def appendAdjacentPoints(stack:list[list[int]], curPoint: tuple[int], pixelArr: list[list[int]]) -> list[list[int]]:
    if(curPoint[0] < len(pixelArr)-1):
        rightPoint = list(curPoint)
        rightPoint[0] += 1 
        stack.append(tuple(rightPoint))
    if(curPoint[0] > 0):
        leftPoint = list(curPoint)
        leftPoint[0] -= 1
        stack.append(tuple(leftPoint))
    if(curPoint[1] < len(pixelArr[0])-1):
        abovePoint = list(curPoint)
        abovePoint[1] += 1
        stack.append(tuple(abovePoint))
    if(curPoint[1] > 0):
        belowPoint = list(curPoint)
        belowPoint[1] -= 1
        stack.append(tuple(belowPoint))
    return stack
