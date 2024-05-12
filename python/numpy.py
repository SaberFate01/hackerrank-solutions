<<<<<<< HEAD
#Arrays
import numpy

#Converts array to a numpy array, a grid of values, like a list but all values must be same type
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


#Shape and Reshape
if __name__ == "__main__":
    n = input()
    arr = n.split(' ') #split int into array
    numpyArr = numpy.array(arr,int) #convert to numpyArr as int
    numpyArr.shape = (3,3) #define shape of numpyArr 3 * 3
    print(numpyArr)
    #print(numpy.reshape(numpyArr,(3,3))) To give a new shape 
    
    """
    [[1 2 3]
    [4 5 6]
    [7 8 9]]
    """

#Transpose and Flatten
import numpy as np

arr = np.array([input().split() for _ in range(int(input().split()[0]))], int)

print(arr.transpose()) #turn the sequence of an array
#([[1,2,3],
#[4,5,6]])
#[[1 4]
 #[2 5]
 #[3 6]]
print(arr.flatten()) #turns the dimensional input to one dimension
=======
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
>>>>>>> d9465b41117bc7f4c58be78b1037ded55fc9b143
