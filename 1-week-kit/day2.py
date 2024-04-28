# Using XOR method to find lonely int in array
def lonelyinteger(a):
    # XOR method
    result = 0
    for number in a:
        result ^= number
    return result


# Finding diff in diagonals of 2D array
def diagonalDifference(arr):
    # Write your code here
    leftDSum = 0
    RightDSum = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            # Left diagonal
            if (i == j):
                leftDSum += arr[i][j]
            # Right diagonal
            if (i+j == len(arr[i])-1):
                RightDSum += arr[i][j]
    if (RightDSum > leftDSum):
        return RightDSum - leftDSum
    else:
        return leftDSum - RightDSum


# Count and return number of times each number appeared:
def countingSort(arr):
    # Write your code here
    tempArr = [0]*(max(arr)+1)
    for i in range(len(arr)):
        tempArr[arr[i]] += 1
    return tempArr

# FizzBuzz: Print different things when multiple of 3 and 5


def fizzBuzz(n):
    # Write your code here

    for i in range(n+1)[1:]:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


# Flipping the matrix to find max sum
#tough as fk how do someone do this in 24 mins
def flippingMatrix(matrix):
    # Write your code here
    rows = len(matrix)
    columns = len(matrix[0])
    value = 0
    for i in range(0, rows//2):
        for j in range(0, columns//2):
            value += max(matrix[i][j], matrix[i][columns-j-1],
                         matrix[rows-1-i][j], matrix[rows-1-i][columns-1-j])
    return value
