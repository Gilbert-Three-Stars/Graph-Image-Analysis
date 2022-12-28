import matplotlib.pyplot as plt
import numpy as np
import math
# This file is going to create a new graph in matplotlib using the points that we found 
# from the image as well as the best fit line.
# 1. Create a graph that has the same dimensions as the downscaled image
# Design q - should we create a new function in graphprocessing that gets the 
# dimensions or should we find them here?
# Neither, we can just find the .size in main and load that into the function we make here.
# 2. plot the points that we got from pointsArr onto the graph.
# 3. Draw the best fit line.

# takes the dimensions from the size of the low res image
def fitToDimensions(dimensions: tuple[int]) ->   plt:
    xArr = [0]
    yArr = [0]
    xIncrement = math.ceil(dimensions[0]/10)
    yIncrement = math.ceil(dimensions[1]/10)
    while(xArr[len(xArr)-1] < dimensions[0]):
        xArr.append(xIncrement + xArr[len(xArr)-1])
    while(yArr[len(yArr)-1] < dimensions[1]):
        yArr.append(yIncrement + yArr[len(yArr)-1])
    plt.plot(xArr, yArr)
    axes = plt.gca()
    axes.set_aspect('equal', adjustable='box')
    return plt

# This function is going to be called after createGraph
# using the pyplot that createGraph generates.
def plotPoints(plot: plt, pointsArr: list[int]) -> plt:
    for point in pointsArr:
        plot.scatter(point[0], point[1])
    return plot

# going to use the best fit line created by BestFitLine
# This will always be called after fitToDimensions and plotPoints
# https://stackoverflow.com/questions/7941226/how-to-add-line-based-on-slope-and-intercept-in-matplotlib
def drawLine(slope: float, intercept: float, plot: plt) -> plt:
    axes = plot.gca()
    xVals = np.array(axes.get_xlim())
    yVals = intercept + slope * xVals
    plot.plot(xVals, yVals, '--')
    axes.lines.pop(0) # removes the line that comes with the plot.
    return plot
