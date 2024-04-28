# Merge two sorted linked lists: Merge 2 linked lists together
def mergeLists(head1, head2):
    alist = []
    blist = []
    while (head1 != None):
        alist.append(head1.data)
        head1 = head1.next
    while (head2 != None):
        blist.append(head2.data)
        head2 = head2.next
    alist = alist + blist
    alist.sort()
    mergeList = SinglyLinkedList()
    for i in range(len(alist)):
        listItem = int(alist[i])
        mergeList.insert_node(listItem)
    return mergeList.head

# Others:


def mergeLists(head1, head2):
    curr = SinglyLinkedListNode(None)
    dummy = curr

    while head1 and head2:
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    if head1:
        curr.next = head1
    if head2:
        curr.next = head2

    return dummy.next


#Queue using two stacks (shld be one stack tbh):

class queue:
    # A queue ADT FIFO structure
    def __init__(self):
        self._data = []*10
        self._size = 0
        self._capacity = 10
        
    def __resize(self) -> None:
        self._capacity *= 2
        new_list = [None] * self._capacity
        for i in range(self._size):
            new_list[i] = self._data[i]
        # Update reference
        self._data = new_list
    
    def enqueue(self, data: any) -> None:
        self._data.append(data)
        self._size += 1
        #print(self._data)
    
    def dequeue(self) -> None:
        if self._size == 0:
            return None
        index = self._size - 1
        value = self._data.pop(0)
        #print(self._data)
        
    def peek(self) -> None:
        return self._data[0]
        
        
if __name__ == "__main__":
    q = int(input())    # no. of queries
    queue = queue()
    for _ in range(q):
        inp = input()
        if " " in inp:
            #print("enqueueing ",inp)
            queue.enqueue(int(inp.split()[1]))
        elif inp == "2":
            #print("dequeue")
            queue.dequeue()
        else:
            #print("peek")
            print(queue.peek())
    


#Balanced Brackets
def isBalanced(s):
    # Write your code here
    openList = ['(','{','[']
    closeList = [')','}',']']
    stack = []  #Used to keep track of unmatched brackets
    for char in s:
        if char in openList: #If character is an open character, append to stack 
            stack.append(char)
        else:
            if not stack: #if stack is empty/ the char not found in openList
                return 'NO'
            id = closeList.index(char) #Finds the index of char in closeList since it is not in openList
            if(stack[-1] == openList[id]): #Check if the last char in stack in closelist matches 
                #stack[-1] access the last element of stack
                stack.pop()
            else:
                return 'NO'
    if stack: #If stack is still not empty.
        return 'NO'
    return 'YES'


# Pairs: Figure out which number - which number = k
def pairs(k, arr):
    # Write your code here
    arr.sort()
    n = len(arr)
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] - arr[i] == k:
                pairs += 1
            elif arr[j] - arr[i] > k:
                # Break here, because subsequent pairs will never be be a pair, no point continuing the loop
                # 2 - 1 = 1 continue
                # 3 - 1 = 2 a pair
                # 4 - 1 = 3 ...
                # 5 - 1 = 4 ... Just break at 3
                break
    return pairs
