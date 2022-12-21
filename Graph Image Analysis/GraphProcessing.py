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

def detectPoints(image: Image, pointsClr: list[list[int]]) -> list[list[int]]:
    pointLocationArr = []
    pixelArr = np.asarray(image)
    for i in range(0, len(pixelArr)):
        for j in range(0, len(pixelArr[i])):
            if(pixelIsAPoint(pixelArr[i][j],pointsClr)):
                pointLocationArr.append([j,imgHeight-i])
    return pointLocationArr
