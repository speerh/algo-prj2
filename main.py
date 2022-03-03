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

temp = unsortedList
tStart = time.time()
bubbleSort(temp)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nUnsorted: " + str(timeElapsed))
print(timeElapsed)

#BUBBLE SORT SORTED
timeElapsed = 0

temp = sortedList
tStart = time.time()
bubbleSort(temp)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nSorted: " + str(timeElapsed))
print(timeElapsed)

#BUBBLE SORT REVERSED
timeElapsed = 0

temp = reverseList
tStart = time.time()
bubbleSort(temp)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nReversed: " + str(timeElapsed))
print(timeElapsed)

#------QUICK SORT------
#Best: O(n log n) - sorted
#Average: O(n log n)
#Worst: O(n^2)
out.write("\n\nQUICK SORT:\n\n")

#QUICK SORT UNSORTED
timeElapsed = 0

temp = unsortedList
tStart = time.time()
quickSort(temp, 0, len(temp) - 1)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nUnsorted: " + str(timeElapsed))
print(timeElapsed)

#QUICK SORT SORTED
timeElapsed = 0

temp = sortedList
tStart = time.time()
quickSort(temp, 0, len(temp) - 1)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nSorted: " + str(timeElapsed))
print(timeElapsed)

#QUICK SORT REVERSED
timeElapsed = 0

temp = reverseList
tStart = time.time()
quickSort(temp, 0, len(temp) - 1)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nReversed: " + str(timeElapsed))
print(timeElapsed)

#------MERGE SORT------
#Best/Worst/Average: O(n log n)
out.write("\n\nMERGE SORT:\n\n")


#MERGE SORT UNSORTED 
timeElapsed = 0

temp = unsortedList
tStart = time.time()
mergeSort(temp)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nUnsorted: " + str(timeElapsed))
print(timeElapsed)

#------RADIX SORT------
out.write("\n\nRADIX SORT:\n\n")

#RADIX SORT UNSORTED
timeElapsed = 0

temp = unsortedList
tStart = time.time()
radixSort(temp)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nUnsorted: " + str(timeElapsed))
print(timeElapsed)

#RADIX SORT SORTED
timeElapsed = 0

temp = sortedList
tStart = time.time()
radixSort(temp)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nSorted: " + str(timeElapsed))
print(timeElapsed)

#RADIX SORT REVERSED
timeElapsed = 0

temp = reverseList
tStart = time.time()
radixSort(temp)
timeElapsed = time.time() - tStart
timeElapsed = round(timeElapsed, 5)
out.write("\nReversed: " + str(timeElapsed))
print(timeElapsed)

