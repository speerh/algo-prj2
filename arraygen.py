#one function for sorted, one function for unsorted
import random

def listGen(length):
    randList = []
    
    for i in range(0, length):
        n = random.randint(1, length)
        randList.append(n)
    return randList