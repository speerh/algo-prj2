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

length = 10000

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
temp = unsortedList
bubbleSort(temp)
out.write("\nUnsorted: ",)

#BUBBLE SORT SORTED
temp = sortedList
bubbleSort(temp)
out.write("\nSorted: ",)

#BUBBLE SORT REVERSED
temp = reverseList
bubbleSort(temp)
out.write("\nReversed: ",)

#------QUICK SORT------
#Best: O(n log n) - sorted
#Average: O(n log n)
#Worst: O(n^2)
out.write("\n\nQUICK SORT:\n\n")

#QUICK SORT UNSORTED
temp = unsortedList
quickSort(temp, 0, len(temp) - 1)
out.write("\nUnsorted: ",)

#QUICK SORT SORTED
temp = sortedList
quickSort(temp, 0, len(temp) - 1)
out.write("\nSorted: ",)

#QUICK SORT REVERSED
temp = reversedList
quickSort(temp, 0, len(temp) - 1)
out.write("\nReversed: ",)

#------MERGE SORT------
#Best/Worst/Average: O(n log n)
out.write("\n\nMERGE SORT:\n\n")


#MERGE SORT UNSORTED
temp = unsortedList
mergeSort(temp)
out.write("\nUnsorted: ",)


