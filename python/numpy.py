#Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    tempArr = []
    for i in range(len(arr)):
        tempArr.append(arr[len(arr)-i-1])
    nump = numpy.array(tempArr,float) #convert to float
    return nump

arr = input().strip().split(' ')
result = arrays(arr)
print(result)