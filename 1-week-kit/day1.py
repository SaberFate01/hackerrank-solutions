def plusMinus(arr):
    # Write your code here
    posCount = 0
    ZeroCount = 0
    negCount = 0

    for i in range(len(arr)):
        if (arr[i] < 0):
            negCount += 1
        elif (arr[i] == 0):
            ZeroCount += 1
        else:
            posCount += 1
    print('{0:.6f}'.format(posCount/len(arr)))
    print('{0:.6f}'.format(negCount/len(arr)))
    print('{0:.6f}'.format(ZeroCount/len(arr)))


# Min Max of array plus together except for one element
def miniMaxSum(arr):
    total_sum = sum(arr)
    # Subtract the max value to get the min sum.
    min_sum = total_sum - max(arr)
    # Subtract the min value to get the max sum.
    max_sum = total_sum - min(arr)
    print(min_sum, max_sum)


# Convert time format

def timeConversion(s):
    # Write your code here
    # check am/pm
    m = s[8:10].upper()
    hour = int(s[0:2])  # Convert the hour part to an integer for comparison
    other = s[2:8]

    if m == 'AM':
        if hour == 12:
            return '00' + other
        else:
            return '{:02d}'.format(hour) + other
    else:  # PM
        if hour != 12:
            hour = hour + 12
        return '{:02d}'.format(hour) + other

# Mock exam: Sort list and find median


def findMedian(arr):
    # Sort the array
    arr.sort()

    n = len(arr)
    # If the number of elements is odd, return the middle element
    if n % 2 != 0:
        return arr[n // 2]
    # If the number of elements is even, return the average of the two middle elements
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2
    