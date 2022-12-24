import sys
from PIL import Image
import numpy as np
import GraphProcessing
import BestFitLine

graphImage1 = Image.open("test_graph_1.png")
lowResGraphImage1 = GraphProcessing.downScaleImage(graphImage1)
pointsArr1 = GraphProcessing.detectPoints(lowResGraphImage1, [[0,0,0]])
graphImage2 = Image.open("test_graph_2.png")
lowResGraphImage2 = GraphProcessing.downScaleImage(graphImage2)
pointsArr2 = GraphProcessing.detectPoints(lowResGraphImage2, [[0,0,0]])
graphImage3 = Image.open("test_graph_3.png")
pointsArr3 = GraphProcessing.detectPoints(graphImage3, [[0,0,0]])
graphImage4 = Image.open("test_graph_4.png")
lowResGraphImage4 = GraphProcessing.downScaleImage(graphImage4)
pointsArr4 = GraphProcessing.detectPoints(lowResGraphImage4, [[20, 100, 185]])
graphImage5 = Image.open("test_graph_5.png")
lowResGraphImage5 = GraphProcessing.downScaleImage(graphImage5)
pointsArr5 = GraphProcessing.detectPoints(lowResGraphImage5, [[0,37,135]])
bestFit1 = BestFitLine.getLine(pointsArr1)
bestFit2 = BestFitLine.getLine(pointsArr2)
bestFit3 = BestFitLine.getLine(pointsArr3)
bestFit4 = BestFitLine.getLine(pointsArr4)
bestFit5 = BestFitLine.getLine(pointsArr5)
# print any of the best fit lines to see their [slope, intercept]

