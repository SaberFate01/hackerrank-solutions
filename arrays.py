def reverseArray(a):
    tempArr = []
    i = 0
    while(i!=len(a)):
        tempArr.append(a[len(a)-i-1])
        i = i +1
    return tempArr

#While loop 2D Array
def hourglassSum(arr):
    # Write your code here
    i = 0
    j = 0
    tempSum = 0
    largestSum = 0
    while(i != 4):
        j = 0 #Reset j to 0 at each new row
        while(j!=4):
            tempSum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+\
                        arr[i+1][j+1] + \
                        arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if tempSum > largestSum:
                largestSum = tempSum
            j+=1 #Increment j
        i+=1 #Increment i
    return largestSum

#For loop 2D Array
def hourglassSum(arr):
    # Write your code here
    i = 0
    j = 0
    tempSum = 0
    largestSum = -63
    for i in range(4):
        for j in range(4):
            tempSum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+\
                        arr[i+1][j+1] + \
                        arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            if tempSum > largestSum:
                largestSum = tempSum
    return largestSum


#Create 2D dynamic array and group according to 2 queries
def dynamicArray(n, queries):
    # Write your code here
    lastAns = 0
    # Creating empty 2D array
    array = [[] for i in range(n)]
    answer = []
    for i in queries:
        type = i[0]
        a = i[1]
        b = i[2]
        #Calculate idx
        idx = (a^lastAns)%n
        
        #When type is 1
        if type == 1:
            array[idx].append(b)  
        #When type is 2, use 2nd query 
        elif type == 2:
            value = array[idx][b%len(array[idx])]
            lastAns = value
            answer.append(lastAns)
            
    return answer


#Rotate to left according to d cycles
def rotateLeft(d, arr):
    # Write your code here
    tempArr = [None]*len(arr)
    n = len(arr)
    for i in range(n):
        #Calculate new index for current elem after d rotations
        newIndex = (i - d) % n
        print(newIndex)
        tempArr[newIndex] = arr[i]
    return tempArr