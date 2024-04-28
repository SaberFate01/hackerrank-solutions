# simple text editor: My wrong ver
# Enter your code here. Read input from STDIN. Print output to STDOUT
class SimpleWord:
    """
    ADT for simple word algorithm
    """

    def __init__(self):
        self._data = []*10
        self._size = 0
        self._capacity = 10
        self._prevAction = []

    def __resize(self) -> None:
        self._capacity *= 2
        new_list = [None] * self._capacity
        for i in range(self._size):
            new_list[i] = self._data[i]
        # Update reference
        self._data = new_list

    def __storePrev(self) -> None:
        self._prevAction.append(self._data[:])

    def append(self, data: any) -> None:
        self.__storePrev()
        if self._size == self._capacity:
            self.__resize
        dataList = list(data)
        for i in dataList:
            self._data.append(i)
        self._size += len(dataList)
        # print('append ',self._data)

    def delete(self, num: int) -> None:
        # Remove num chars starting from back
        self.__storePrev()
        for i in range(self._size, 0, -1):
            # print(i,self._size)
            self._data.pop()
        self._size -= 1
       # print('delete ',self._data)

    def printWord(self, num: int) -> None:
        print(self._data[int(num)-1])

    def undo(self) -> None:
        if not self._prevAction:
            return
        self._data = self._prevAction.pop()  # Restore the last action
        self._size = len(self._data)  # Update size


if __name__ == "__main__":
    userInput = int(input())
    word = SimpleWord()
    for _ in range(userInput):
        inp = input()
        if '1' == inp.split()[0]:
            word.append(inp.split()[1])
        elif '2' == inp.split()[0]:
            # print('inpt del', inp)
            word.delete(inp.split()[1])
        elif '3' == inp.split()[0]:
            word.printWord(inp.split()[1])
        elif '4' == inp.split()[0]:
            # print('undo')
            word.undo()
        else:
            print('invalid input')

# simple text editor: answer:
if __name__ == "__main__":
    Q = int(input())
    char = ""
    temp = []  # temp arr for undo
    for _ in range(Q):
        ops = input().split(" ")
        if ops[0] == "1":
            # append
            temp.append(char)
            char += ops[1]
        elif ops[0] == "2":
            # delete
            temp.append(char)
            # Slice char from index 0 to length of char - input index
            char = char[0:len(char) - int(ops[1])]
        elif ops[0] == "3":
            # print
            print(char[int(ops[1]) - 1])  # print ops -1
        elif ops[0] == "4":
            # undo
            char = temp.pop()  # remove last element in temp list

#jesse and cookies
import heapq
def cookies(k, A):
    heapq.heapify(A) 
    oper = 0 
    while True : 
        last = heapq.heappop(A)
        if last >=k : 
            return oper 
        if last<k and len(A)<1: 
            return -1      
        prelast = heapq.heappop(A)
        new_val = last + prelast*2
        heapq.heappush(A,new_val)
        oper = oper + 1


#Lego bricks: Not mine, never managed to solve it:
        

P = [0,1,2,4,8]
allS = dict()
allT = dict()
for i in range(5,1001):
    P.append(P[i-1] + P[i-2] + P[i-3] + P[i-4])

def legoBlocks(n, m):
    UPPER = 1000000007
    # Total number of layouts is P^n,
    # number of good layouts is S
    T = [0,1]
    S = [0,1]
    if m == 1:
        return 1
    if n == 1:
        if m < 5:
            return 1
        else:
            return 0

    start = 2
    if n in allS:
        S = allS[n]
        if len(S) > m:
            return S[m]
        start = len(S)
        T = allT[n]
            
    for i in range(start,m+1):
        T.append(pow(P[i],n,UPPER))
    allT[n] = T
    for i in range(start,m+1):
        S.append(T[i])
        for j in range(i):
            S[i] -= S[j]*T[i-j]
        S[i]=int(S[i]%UPPER)
    allS[n] = S
    
    return int(S[m]%UPPER)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()