import math
import os
import random
import re
import sys

# Python If-Else
if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2) != 0:
        print("Weird")
    elif (n % 2) == 0:
        if (n >= 2 and n <= 5):
            print("Not Weird")
        if (n >= 6 and n <= 20):
            print("Weird")
        if (n > 20):
            print("Not Weird")

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a + b)
    print(a - b)
    print(a * b)


#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)#floor division
    print(a/b)


#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(pow(i,2)) #To power of 2
#Write a function
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    else:
        if year % 4 == 0:
            leap = True
    
    
    return leap

year = int(input())
print(is_leap(year))

#Print function
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1,end="") #print on same line