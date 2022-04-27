from ast import Num
from calendar import month
from heapq import merge
import random
import time
import pickle
import copy
import plotly.graph_objects as go


mapa = pickle.load(open("mapa.pickle", "rb"))

print(mapa)

potencias = [100, 1000, 10000, 50000, 110000]

quickSortAvgRandomData = []
quickSortAvgAscendingData = []
quickSortAvgDescendingData = []

mergeSortAvgRandomData = []
mergeSortAvgAscendingData = []
mergeSortAvgDescendingData = []

heapSortAvgRandomData = []
heapSortAvgAscendingData = []
heapSortAvgDescendingData = []



for name in mapa:
    for order in mapa[name]:
        for power in mapa[name][order]:
            addition = sum(mapa[name][order][power]["values"])
            if(len(mapa[name][order][power]["values"]) != 0):

                mapa[name][order][power]["avg"] = addition / len(mapa[name][order][power]["values"])

                average = mapa[name][order][power]["avg"]

                if(name == "heapSort"):
                    if(order == "random"):
                        heapSortAvgRandomData.append(average)
                    elif(order == "ascending"):
                        heapSortAvgAscendingData.append(average)
                    else:
                        heapSortAvgDescendingData.append(average)
                elif(name == "quickSort"):
                    if(order == "random"):
                        quickSortAvgRandomData.append(average)
                    elif(order == "ascending"):
                        quickSortAvgAscendingData.append(average)
                    else:
                        quickSortAvgDescendingData.append(average)
                else:
                    if(order == "random"):
                        mergeSortAvgRandomData.append(average)
                    elif(order == "ascending"):
                        mergeSortAvgAscendingData.append(average)
                    else:
                        mergeSortAvgDescendingData.append(average)



                print(mapa[name][order][power]["values"])



                print(addition / len(mapa[name][order][power]["values"]))

print(mapa)
print(quickSortAvgRandomData)
print(quickSortAvgAscendingData)
print(quickSortAvgDescendingData)

fig1 = go.Figure()
mergeGraph = go.Figure()
heapGraph = go.Figure()
quickGraph = go.Figure()



fig1.add_trace(go.Scatter(x = potencias, y = mergeSortAvgRandomData, name = 'Merge Sort Random Order Average', line = dict(color='red', width=4)))
fig1.add_trace(go.Scatter(x = potencias, y = mergeSortAvgAscendingData, name = 'Merge Sort Ascending Order Average', line = dict(color='red', width=4, dash='dash')))
fig1.add_trace(go.Scatter(x = potencias, y = mergeSortAvgDescendingData, name = 'Merge Sort Descending Order Average', line = dict(color='red', width=4, dash='dashdot')))
mergeGraph.add_trace(go.Scatter(x = potencias, y = mergeSortAvgRandomData, name = 'Merge Sort Random Order Average', line = dict(color='red', width=4)))
mergeGraph.add_trace(go.Scatter(x = potencias, y = mergeSortAvgAscendingData, name = 'Merge Sort Ascending Order Average', line = dict(color='red', width=4, dash='dash')))
mergeGraph.add_trace(go.Scatter(x = potencias, y = mergeSortAvgDescendingData, name = 'Merge Sort Descending Order Average', line = dict(color='red', width=4, dash='dash')))

fig1.add_trace(go.Scatter(x = potencias, y = heapSortAvgRandomData, name = 'Heap Sort Random Order Average', line = dict(color='green', width=4)))
fig1.add_trace(go.Scatter(x = potencias, y = heapSortAvgAscendingData, name = 'Heap Sort Ascending Order Average', line = dict(color='green', width=4, dash='dash')))
fig1.add_trace(go.Scatter(x = potencias, y = heapSortAvgDescendingData, name = 'Heap Sort Descending Order Average', line = dict(color='green', width=4, dash='dashdot')))
heapGraph.add_trace(go.Scatter(x = potencias, y = heapSortAvgRandomData, name = 'Heap Sort Random Order Average', line = dict(color='green', width=4)))
heapGraph.add_trace(go.Scatter(x = potencias, y = heapSortAvgAscendingData, name = 'Heap Sort Ascending Order Average', line = dict(color='green', width=4, dash='dash')))
heapGraph.add_trace(go.Scatter(x = potencias, y = heapSortAvgDescendingData, name = 'Heap Sort Descending Order Average', line = dict(color='green', width=4, dash='dashdot')))

fig1.add_trace(go.Scatter(x = potencias, y = quickSortAvgRandomData, name = 'Quick Sort Random Order Average', line = dict(color='blue', width=4)))
fig1.add_trace(go.Scatter(x = potencias, y = quickSortAvgAscendingData, name = 'Quick Sort Ascending Order Average', line = dict(color='blue', width=4, dash='dash')))
fig1.add_trace(go.Scatter(x = potencias, y = quickSortAvgDescendingData, name = 'Quick Sort Descending Order Average', line = dict(color='blue', width=4, dash='dashdot')))
quickGraph.add_trace(go.Scatter(x = potencias, y = quickSortAvgRandomData, name = 'Quick Sort Random Order Average', line = dict(color='blue', width=4)))
quickGraph.add_trace(go.Scatter(x = potencias, y = quickSortAvgAscendingData, name = 'Quick Sort Ascending Order Average', line = dict(color='blue', width=4, dash='dash')))
quickGraph.add_trace(go.Scatter(x = potencias, y = quickSortAvgDescendingData, name = 'Quick Sort Descending Order Average', line = dict(color='blue', width=4, dash='dashdot')))


fig1.show()
mergeGraph.show()
heapGraph.show()
quickGraph.show()


