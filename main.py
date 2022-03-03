import time
from arraygen import *
from sorts import *
'''
create array to feed into sort
function to create unsorted
function to create already sorted
size?

bubble sort unsorted, sorted

quick sort unsorted, sorted

merge sort

??? sort
'''

length = 1000

unsortedList = listGen(length)
sortedList = listGen(length)
reverseList = listGen(length)

sortedList.sort()
reverseList.sort()
reverseList.reverse()

out = open('out.txt', 'w')

#------BUBBLE SORT------
#Best: O(n) - sorted
#Average: O(n^2)
#Worst: O(n^2)
out.write("BUBBLE SORT:\n\n")

#BUBBLE SORT UNSORTED
timeElapsed = 0
tStart = time.time()
temp = unsortedList
bubbleSort(temp)
out.write("\nUnsorted: ",)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
print(timeElapsed)

#BUBBLE SORT SORTED
timeElapsed = 0
tStart = time.time()
temp = sortedList
bubbleSort(temp)
out.write("\nSorted: ",)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
print(timeElapsed)

#BUBBLE SORT REVERSED
timeElapsed = 0
tStart = time.time()
temp = reverseList
bubbleSort(temp)
out.write("\nReversed: ",)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
print(timeElapsed)

#------QUICK SORT------
#Best: O(n log n) - sorted
#Average: O(n log n)
#Worst: O(n^2)
out.write("\n\nQUICK SORT:\n\n")

#QUICK SORT UNSORTED
timeElapsed = 0
tStart = time.time()
temp = unsortedList
quickSort(temp, 0, len(temp) - 1)
out.write("\nUnsorted: ",)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
print(timeElapsed)

#QUICK SORT SORTED
timeElapsed = 0
tStart = time.time()
temp = sortedList
quickSort(temp, 0, len(temp) - 1)
out.write("\nSorted: ",)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
print(timeElapsed)

#QUICK SORT REVERSED
timeElapsed = 0
tStart = time.time()
temp = reverseList
quickSort(temp, 0, len(temp) - 1)
out.write("\nReversed: ",)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
print(timeElapsed)

#------MERGE SORT------
#Best/Worst/Average: O(n log n)
out.write("\n\nMERGE SORT:\n\n")


#MERGE SORT UNSORTED 
timeElapsed = 0
tStart = time.time()
temp = unsortedList
mergeSort(temp)
out.write("\nUnsorted: ",)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
print(timeElapsed)

