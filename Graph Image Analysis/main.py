import sys
from PIL import Image
import numpy as np
import random
import GraphProcessing
import MathCalculations
import TheilSenEstimator
np.set_printoptions(threshold=sys.maxsize)

pointsColor = [random.randint(0,255),random.randint(0,255),random.randint(0,255),255]
whitespaceColor = [random.randint(0,255),random.randint(0,255),random.randint(0,255),255]
lineColor = [random.randint(0,255),random.randint(0,255),random.randint(0,255),255]
graphImage1 = Image.open("/Users/gilbert/Desktop/code/Personal Project/test_graph_1.png")
processedGraph = GraphProcessing.processGraph(graphImage1, pointsColor, whitespaceColor, lineColor)
pointsArr = GraphProcessing.detectPoints(processedGraph, pointsColor)
print(TheilSenEstimator.getLine(pointsArr))

