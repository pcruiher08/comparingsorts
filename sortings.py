from ast import Num
from calendar import month
from heapq import merge
import random
import time
import pickle
import copy
import plotly.graph_objects as go


def QSPartition(arr, low, high):
    i = (low-1)
    pivot = arr[high]
 
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 
def quickSort(arr):
    tic = time.perf_counter()
    quickSortUtility(arr, 0, len(arr)-1)
    tac = time.perf_counter()
    return tac - tic

def quickSortUtility(arr, low, high):

    size = high - low + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    while top >= 0:

        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        p = QSPartition( arr, low, high )
 
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1
 
        if p + 1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high
 
 

def mergeSort(arr):
    tic = time.perf_counter()
    mergeSortUtility(arr)
    tac = time.perf_counter()

    return tac - tic

def mergeSortUtility(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSortUtility(L)
        mergeSortUtility(R)
  
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
 
def fix(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
 
    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r
 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
 
        fix(arr, n, largest)

def heapSort(arr):
    tic = time.perf_counter()
    heapSortUtility(arr)
    tac = time.perf_counter()
    return tac - tic
 
def heapSortUtility(arr):
    n = len(arr)
 
    for i in range(n//2 - 1, -1, -1):
        fix(arr, n, i)
 
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        fix(arr, i, 0)
 

def generateArrayOfSizeN(N):
    arr = []
    for i in range(N):
        num = random.randint(1,150)
        arr.append(num)
    return arr

base = 10

mapa = {
    "quickSort" : {
        "random" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        },
        "ascending" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        },
        "descending" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        }
    },
    "mergeSort" : {
        "random" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        },
        "ascending" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        },
        "descending" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        }
    },
    "heapSort" : {
        "random" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        },
        "ascending" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        },
        "descending" : {
            "2" : {"values" : [], "avg" : Num},
            "3" : {"values" : [], "avg" : Num},
            "4" : {"values" : [], "avg" : Num},
            "5" : {"values" : [], "avg" : Num},
            "6" : {"values" : [], "avg" : Num}
        }
    }
}

for power in range(2, 7):
    for iteration in range(1, 2):

        if(power < 5):
            randomArr1 = generateArrayOfSizeN(10**power)
        else:
            if(power == 5):
                randomArr1 = generateArrayOfSizeN(10000*power)
            if(power == 6):
                randomArr1 = generateArrayOfSizeN(10000*(power+5))

        randomArr2 = copy.deepcopy(randomArr1)
        randomArr3 = copy.deepcopy(randomArr2)
        #print(arr1)
        #print(arr2)
        #print(arr3)
        mapa["quickSort"]["random"][str(power)]["values"].append(quickSort(randomArr1))
        mapa["mergeSort"]["random"][str(power)]["values"].append(mergeSort(randomArr2))
        mapa["heapSort"]["random"][str(power)]["values"].append(heapSort(randomArr3))

        ascendingArr1 = randomArr1
        ascendingArr2 = copy.deepcopy(randomArr1)
        ascendingArr3 = copy.deepcopy(randomArr2)

        mapa["quickSort"]["ascending"][str(power)]["values"].append(quickSort(randomArr1))
        mapa["mergeSort"]["ascending"][str(power)]["values"].append(mergeSort(randomArr2))
        mapa["heapSort"]["ascending"][str(power)]["values"].append(heapSort(randomArr3))

        descendingArr1 = ascendingArr1.reverse()
        descendingArr2 = copy.deepcopy(descendingArr1)
        descendingArr3 = copy.deepcopy(descendingArr2)

        mapa["quickSort"]["descending"][str(power)]["values"].append(quickSort(randomArr1))
        mapa["mergeSort"]["descending"][str(power)]["values"].append(mergeSort(randomArr2))
        mapa["heapSort"]["descending"][str(power)]["values"].append(heapSort(randomArr3))  
        #print(arr1)
        #print(arr2)
        #print(arr3)

        print(power, iteration, sep=", ")

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

with open('mapa.pickle', 'wb') as handle:
    pickle.dump(mapa, handle, protocol=pickle.HIGHEST_PROTOCOL)

