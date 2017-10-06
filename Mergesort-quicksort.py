#!/usr/bin/env python2.7
# Ankita Alshi - 24th Sep 2017
#
# Insertion sort, Merge sort and quick sort implementation in Python:
#
import datetime
import time
import random
import sys
import matplotlib.pyplot as plt

######################## Insertion Sort ##############################

# Sort the given input list and calculate execution time
def insertion_sort(a):
    # Select 1 element at a time and compare it with the elements on its left. 
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        # If key is less than a[i], move a[i] to its right
        # and keep checking elements on left.
        while (i >= 0 and a[i] > key):
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key
    return 

############################### Merge Sort ############################

# Merge sort to sort gievn input list and calculate execution time
def merge_sort(a, p, r):
    
    if (p < r):
        # Caluculate Mid of list
        q = int((p + r) / 2)
        if (q < 0):
            return
        # Recursive call to sort n/2 list
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        # Merge the to n/2 list
        merge(a, p, q, r)
    return

# Merge the sorted lists
def merge(a, p, q, r):
    
    # Calculate length of left and right arrays
    n1 = q - p + 1
    n2 = r - q
    L = [0 for x in range(n1)]
    R = [0 for x in range(n2)]

    # Store elements in left array from p to q of list a
    for i in range(0, n1):
        L[i] = a[p + i]
        
    # Store elements in right array from q + 1 to r of list a
    for j in range(0, n2):
        R[j] = a[q + j + 1]
        
    # Set last element of both left and right arrays to be more than possible value which is n (infinity)
    L.append(int(n) + 100)
    R.append(int(n) + 100)

    # Set i and jto start of left and right array
    i = 0
    j = 0
    
    # Copy smallest element at a time from left and right array to "a" back.
    for k in range(p, r + 1):
        if (L[i] < R[j]):
            a[k] = L[i]
            i = i + 1
        else:
            a[k] = R[j]
            j = j + 1
    
    return

############################### Quick Sort ############################

# Quick sort to sort gievn input list and calculate execution time
def quick_sort(a, p, r):
    if (p < r):
        # key on which array is partitioned 
        q = partition(a, p, r)
        # Recursive call
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)
    return

def partition(a, p, r):
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if (a[j] <= x):
            i = i + 1
            temp1 = a[i]
            a[i] = a[j]
            a[j] = temp1
    temp2 = a[i + 1]
    a[i + 1] = a[r]
    a[r] = temp2
    return i + 1

############################# Execution of Insertion Sort ##################

# Function to call Insertion sort
def exec_insertion_sort(b):
    for i in range(num):
        a = [val for val in b]
        if (i == 0):
            #Time before the sorting starts
            t1 = datetime.datetime.now()
            insertion_sort(a)
            t2 = datetime.datetime.now()
            t = t2 - t1
        else:
            #Time before the sorting starts
            t1 = datetime.datetime.now()
            insertion_sort(a)
            t2 = datetime.datetime.now()
            t = t + (t2 - t1)
    

    #Print average time for insertion sort to sort random numbers input
    print ('Insertion Sort: Average time to sort: ', t / num)
    return (t / num).total_seconds()

############################## Execution of Merge Sort #######################

# Function to call Merge sort
def exec_merge_sort(b):
    for i in range(num):
        a = [val for val in b]
        if (i == 0):
            #Time before the sorting starts
            t1 = datetime.datetime.now()
            merge_sort(a, 0, len(a) - 1)
            t2 = datetime.datetime.now()           
            t = t2 - t1 
        else:
            #Time before the sorting starts
            t1 = datetime.datetime.now()
            merge_sort(a, 0, len(a) - 1)
            t2 = datetime.datetime.now() 
            t = t + (t2 - t1)

    #Print average time for Merge sort to sort random numbers input
    print ('Merge Sort: Average time to sort: ', t / num)
    return (t / num).total_seconds()

############################## Execution of Quick Sort #######################

# Function to call Quick sort
def exec_quick_sort(b):
    for i in range(num):
        a = [val for val in b]
        if (i == 0):
            #Time before the sorting starts
            t1 = datetime.datetime.now()
            quick_sort(a, 0, len(a) - 1)
            t2 = datetime.datetime.now()           
            t = t2 - t1 
        else:
            #Time before the sorting starts
            t1 = datetime.datetime.now()
            quick_sort(a, 0, len(a) - 1)
            t2 = datetime.datetime.now() 
            t = t + (t2 - t1)

    #Print average time for Quick sort to sort random numbers input
    print ('Quick Sort: Average time to sort: ', t / num)
    return (t / num).total_seconds()
    
##################################### Main ###################################    

def main():
    
    #number of iterations  
    global num
    num = 10
    global n

    # List to store x points (data points value) for ploting the graph. 
    x = []

    # initialize lists to store avg time taken by all three algorithms for plots 
    yraninsert = []
    yranmerge = []
    yranquick = []
    yincinsert = []
    yincmerge = []
    yincquick = []
    ydecinsert = []
    ydecmerge = []
    ydecquick = []

    # Data points - Input from command line
    print ("Enter data points")  
    data_set = sys.argv[1]
    num_input = data_set.split(",")

    # Set recursion limit to avoid stack overflow
    sys.setrecursionlimit(20000)
    

    for n in num_input:

        print ("for data point : ", n)
        # Create list of n random numbers
        b = [random.randint(1, int(n)) for i in range(0, int(n))]

        x.append(n)
    
        # Function to call Insertion sort function 10 times with random input
        yraninsert.append(exec_insertion_sort(b))

        # Function to call Merge sort function 10 times with random input
        yranmerge.append(exec_merge_sort(b))

        # function to call Quick sort function 10 times with random input
        yranquick.append(exec_quick_sort(b))
#########################################################################

        # Sort the array to make non-decreasing input
        b.sort()
       
        # Function to call Insertion sort function 10 times with non-decreasing input
        yincinsert.append(exec_insertion_sort(b))

        # Function to call Merge sort function 10 times with non-decreasing input
        yincmerge.append(exec_merge_sort(b))

        # Function to call Quick sort function 10 times with random input
        yincquick.append(exec_quick_sort(b))
#########################################################################

        # Reverse the list to make non-increasing input
        b.reverse()
       
        # Function to call Insertion sort function 10 times with non-increasing input
        ydecinsert.append(exec_insertion_sort(b))

        # Function call Merge sort function 10 times with non-increasing input
        ydecmerge.append(exec_merge_sort(b))
    
        # function to call Quick sort function 10 times with random input
        ydecquick.append(exec_quick_sort(b))

    # Plot the graph for random inputs for all three algorithms 
    plt.figure(0)
    plt.plot(x, yraninsert, color='red', label='insert')
    plt.plot(x, yranmerge, color='green', label='merge')
    plt.plot(x, yranquick, color='blue', label='quick')
    plt.ylabel('Time in seconds')
    plt.xlabel('Data Points')
    plt.title('Random Numbers')
    plt.legend()
    plt.show()

    # Plot the graph for non-decreasing inputs for all three algorithms 
    plt.figure(1)
    plt.plot(x, yincinsert, color='red', label='insert')
    plt.plot(x, yincmerge, color='green', label='merge')
    plt.plot(x, yincquick, color='blue', label='quick')
    plt.ylabel('Time in seconds')
    plt.xlabel('Data Points')
    plt.title('Non-decreasing Numbers')
    plt.legend()
    plt.show() 

    # Plot the graph for non-increasing inputs for all three algorithms 
    plt.figure(2)
    plt.plot(x, ydecinsert, color='red', label='insert')
    plt.plot(x, ydecmerge, color='green', label='merge')
    plt.plot(x, ydecquick, color='blue', label='quick')
    plt.ylabel('Time in seconds')
    plt.xlabel('Data Points')
    plt.title('Non-increasing Numbers')
    plt.legend()
    plt.show()

########################################################################
        
if __name__== "__main__":
  main()



