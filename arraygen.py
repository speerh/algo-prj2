#one function for sorted, one function for unsorted
import random

def listGen():
    randList = []
    
    for i in range(0,10000):
        n = random.randint(1, 10000 + 1)
        randList.append(n)
    return randList