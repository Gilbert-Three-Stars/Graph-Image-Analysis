import numpy as np
import GraphProcessing
import BestFitLine
import CreateGraph
np.set_printoptions(threshold=sys.maxsize)

graphImage1 = Image.open("test_graph_1.png")
lowResGraphImage1 = GraphProcessing.downScaleImage(graphImage1)
pointsArr1 = GraphProcessing.createPoints(lowResGraphImage1, [[0,0,0]], GraphProcessing.pointSize(lowResGraphImage1, [[0,0,0]]))
graphImage2 = Image.open("test_graph_2.png")
lowResGraphImage2 = GraphProcessing.downScaleImage(graphImage2)
pointsArr2 = GraphProcessing.createPoints(lowResGraphImage2, [[0,0,0]], GraphProcessing.pointSize(lowResGraphImage2, [[0,0,0]]))
graphImage3 = Image.open("test_graph_3.png")
lowResGraphImage3 = GraphProcessing.downScaleImage(graphImage3)
pointsArr3 = GraphProcessing.createPoints(lowResGraphImage3, [[0,0,0]], GraphProcessing.pointSize(lowResGraphImage3, [[0,0,0]]))
graphImage4 = Image.open("test_graph_4.png")
lowResGraphImage4 = GraphProcessing.downScaleImage(graphImage4)
pointsArr4 = GraphProcessing.createPoints(lowResGraphImage4, [[20, 100, 185]], GraphProcessing.pointSize(lowResGraphImage4, [[20, 100, 185]]))
graphImage5 = Image.open("test_graph_5.png")
lowResGraphImage5 = GraphProcessing.downScaleImage(graphImage5)
pointsArr5 = GraphProcessing.createPoints(lowResGraphImage5, [[0,37,135]], GraphProcessing.pointSize(lowResGraphImage5, [[0,37,135]]))
bestFit1 = BestFitLine.getLine(pointsArr1)
bestFit2 = BestFitLine.getLine(pointsArr2)  
bestFit3 = BestFitLine.getLine(pointsArr3)
bestFit4 = BestFitLine.getLine(pointsArr4)
bestFit5 = BestFitLine.getLine(pointsArr5)
# plot1 = CreateGraph.createPlot(lowResGraphImage1.size, bestFit1[0], bestFit1[1], pointsArr1)
# plot2 = CreateGraph.createPlot(lowResGraphImage2.size, bestFit2[0], bestFit2[1], pointsArr2)
# plot3 = CreateGraph.createPlot(lowResGraphImage3.size, bestFit3[0], bestFit3[1], pointsArr3)
# plot4 = CreateGraph.createPlot(lowResGraphImage4.size, bestFit4[0], bestFit4[1], pointsArr4)
plot5 = CreateGraph.createPlot(lowResGraphImage5.size, bestFit5[0], bestFit5[1], pointsArr5)
plot5.show() 

