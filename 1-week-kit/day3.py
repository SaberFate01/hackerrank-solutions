# Changing to zig zag pattern, example 1 2 3 4 5 6 7 to 1 2 3 7 6 5 4
def findZigZagSequence(a, n):
    a.sort()  # 1,2,3,4,5,6,7
    mid = int((n)//2)  # 3
    a[mid], a[n-1] = a[n-1], a[mid]  # mid:4,end:7 -> mid:7, end:4

    st = mid + 1  # 4
    ed = n - 2  # 6
    while (st <= ed):  # start <= end
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return

# Tower breaker games, if takes even moves, P2 wins, if takes odd moves, P1 wins, due to the nature
# Of the game, as game is deterministic and both player play optimally


def towerBreakers(n, m):
    # Write your code here
    towers = n*[m]
    while True:
        if (m == 1):
            return 2
        elif (n % 2 == 0):
            return 2
        else:
            return 1

# Caesar Cipher: Move each letter by three letters down the 26 alphabets

def caesarCipher(s, k):
    # Write your code here
    stringArr = list(s)#Convert string to list
    letters = "abcdefghijklmnopqrstuvwxyz"
    letterArr = list(letters)
    lettersCap = list(letters.upper())
    tempArr = []
    length = len(tempArr)
    k = k % 26 #This line important! if k > 26!
    for i in range(len(stringArr)):
        newPos = 0 # Define& refresh postion of letter
        if stringArr[i].isalpha() == False:
            tempArr.append(stringArr[i])
        elif stringArr[i].isupper() == True:
            for j in range(len(lettersCap)):
                if(lettersCap[j]==stringArr[i]):
                    #print('j',j)
                    newPos = j + k
                    #print(newPos)
                    if newPos > 25:
                        newPos = newPos-26
            tempArr.append(lettersCap[newPos])
        else:
            for j in range(len(letterArr)):
                if(letterArr[j]==stringArr[i]):
                    newPos = j + k
                    if newPos > 25:
                        newPos = newPos-26
            tempArr.append(letterArr[newPos])
    string = "".join(tempArr)
    return string
    #        newPos = i - k
    #    if newPos < 0:
    #       newPos = length + newPos
    #    tempArr[newPos] = stringArr[i]
            

#PalindromeIndex: My wrong version
def palindromeIndex(s):
    # Write your code here
    arr = s.split('\n')
    reversed = []
    for i in range(len(arr)):
        word = list(arr[i])
        reverse2 = word[::-1]
        reverse2 = "".join(reverse2)
        reversed.append(reverse2)
    for j in range(len(arr)):
        if arr[j] == reversed[j]:
            return -1
        else:
            reversedWord = list(reversed[j])
            word = list(arr[j])
            diffAlphabet = 0
            location = 0
            for r in range(len(reversedWord)-1):
                print(len(reversedWord),len(word),r)
                if reversedWord[r]!= word[r]:
                    word.pop(r)
                    #print(r,len(reversedWord)-r)
                    reversedWord.pop(len(reversedWord)-r-1)
                    location = r
            reversedWord = "".join(reversedWord)
            word = "".join(word)
            if(word == reversedWord):
                print(word,reversedWord)
                return r
            else:
                print(word,reversedWord)

#Correct Version
def palindromeIndex(s):
    # Check if the word is already a palindrome
    if s == s[::-1]:
        return -1
    
    # Check for the character that, when removed, results in a palindrome
    for i in range(len(s)):
        # Try skipping the character at index i and check if it forms a palindrome
        if s[i] != s[-(i+1)]:
            # Form a string without the ith character
            without_i = s[:i] + s[i+1:]
            # Check if the string without the ith character is a palindrome
            if without_i == without_i[::-1]:
                return i
            else:
                # If removing the ith character from the start does not work,
                # it means the corresponding character at the end is the one to remove
                return len(s) - 1 - i
    return -1