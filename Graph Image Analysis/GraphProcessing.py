import sys
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

def pixelIsAPoint(pixel, pixelColors):
    pixel = [pixel[0], pixel[1], pixel[2]]
    for i in range (0, len(pixelColors)):
        curColor = pixelColors[i]
        if(pixelColorMatch(curColor, pixel)): return True
    return False

def pixelColorMatch(p1, p2):
    for i in range(0, len(p1)):
        if(abs(p1[i]-p2[i]) > 10):
            return False
    return True    

def detectPoints(image, pointsClr):
    pointLocationArr = []
    pixelArr = np.asarray(image)
    for i in range(0, len(pixelArr)):
        for j in range(0, len(pixelArr[i])):
            if(pixelIsAPoint(pixelArr[i][j],pointsClr)):
                pointLocationArr.append([i,j])
    return pointLocationArr
