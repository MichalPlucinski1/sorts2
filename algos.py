import random
import time
from enum import Enum
import numpy as np
import matplotlib . pyplot as plot
import sys
import threading

threading.stack_size(67108864) #64MB
sys.setrecursionlimit(2 ** 20)



############################# sorts #############################

#Insertion Sort
def iS(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort
def sS(arr):
# Traverse through all array elements
    for i in range(len(arr)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Heap Sort (auxiliary function)
def heapify(arr, N, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < N and arr[largest] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, N, largest)

# Heap Sort (main hS function)
def hS(arr):
    N = len(arr)

    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        heapify(arr, N, i)

    # One by one extract elements
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Merge Sort
def mS(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mS(L)
  
        # Sorting the second half
        mS(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

############################# usage functions #############################

#just separation from other entitis
def programStart():
    for i in range(4):
        print("---program start---")



#filling tab with const or randoms
def tabFill(arr, l=10, v=1, rand = True):
    append = arr.append
    if rand == True: # filling with randoms
        for i in range(0, l): #packing tab
            append(random.randrange(1, v + 1)) #from 1 to valuemax
    else:
        for i in range(0, l): #packing tab 
            append(v)   


#function measuring time of actions in parameters
def mTime(arr, mysort):
    avg = 0
    iterations = repetitions
    for i in range(iterations):
        start_time = time.time()
        mysort(arr.copy())
        stop_time = time.time() - start_time
        avg += stop_time 

    stop_time = avg/iterations
    return stop_time



#making graphs
def plotting(rv, ascv, descv, constv, vv, vTime, title):
    #linear
    plot.figure()
    plot.plot(vTime,rv, vTime, ascv,vTime, descv, vTime, constv, vTime, vv)
    plot.title(title)
    plot.xlabel('number of sorts')
    plot.ylabel('time[s]')
    plot.legend([ "rand", "asc", "desc", "const", "vShaped"])
    plot.grid(True)

    #logarithm
    plot.figure()
    plot.plot(vTime,rv, vTime, ascv,vTime, descv, vTime, constv, vTime, vv)
    plot.yscale('log')
    plot.title(str(title + ' log'))
    plot.xlabel('number of sorts')
    plot.ylabel('time[s]')
    plot.legend([ "iS","sS","hS","mS","vv"])
    plot.grid(True) 

    

#generating v-shaped
def vSFillTab(l, low_num_tabs):
    for i in range(1,low_num_tabs,2):
        l.append(i)
        l.insert(0, i+1)

#updating v-shaped
def vSAddToTab(l, step):
     step = int(step/2)
     for i in range(step):
        first_num = l[0]
        l.append(first_num+1)
        l.insert(0, first_num + 2)

def mysort(r, vTime, rv, ascv, descv, constv, vv, sorts):
    for i in range(startValue, endValue, step):
            vTime.append(i) #making y dimmension for plot
            print("Filling randoms, len of arr: ", len(r), " of ", endValue)
            ## random
            rv.append(mTime(r, sorts))

            ##sorted
            r.sort()
            ascv.append(mTime(r, sorts))

            ##sorted desc
            r.sort(reverse=True)
            descv.append(mTime(r, sorts))
            del r


            ## const
            r = []
            tabFill(r, i, 1)
            constv.append(mTime(r, sorts))
            del r

            ## V-shaped
            r = []
            vSFillTab(r, i)
            vv.append(mTime(r, sorts))
    
        
            print("end of this iteration \n")

def deletions(a, b, c, d, e):
    del a
    del b
    del c
    del d
    del e

def popping(rv,ascv,descv,constv, vv,vTime):
    rv.pop(0)
    ascv.pop(0)
    descv.pop(0)
    constv.pop(0)
    vv.pop(0)
    vTime.pop(0)
############################# main #############################

def main():
    programStart()
    

    #array settings
    r = []
    #l = 5000 #length of array  # overwritten by 
    global v
    v = 150 #max value in array

    
    #loop of 1 sort settings
    global startValue 
    startValue = 2000 #750 
    global endValue 
    endValue = 3500 #3000
    global step 
    step = 100 #2  #50
    global repetitions
    repetitions= 5 #to generate avg


    #bufored times
    rv = []
    ascv = []
    descv = []
    constv = []
    vv = []
    vTime = []

    print("startValue: ", startValue, " endValue: ", endValue, " with step: ", step)

    ################### for iS ###################
    mysort(r, vTime, rv, ascv, descv, constv, vv, iS)
    
    print("end of this iteration \n")
    #print(results)

    
    plotting(rv,ascv,descv,constv, vv,vTime, "iS")

    deletions(rv,ascv,descv,constv,vTime)


    ################### for Hs ###################
    rv = []
    ascv = []
    descv = []
    constv = []
    vv = []
    vTime = []
    mysort(r, vTime, rv, ascv, descv, constv, vv, hS)
    
    print("end of this iteration \n")
    #print(results)

    popping(rv,ascv,descv,constv, vv,vTime)
    plotting(rv,ascv,descv,constv, vv,vTime, "hS")

    deletions(rv,ascv,descv,constv,vTime)

    
    ################### for ss ###################
    rv = []
    ascv = []
    descv = []
    constv = []
    vv = []
    vTime = []
    mysort(r, vTime, rv, ascv, descv, constv, vv, sS)
    
    print("end of this iteration \n")
    #print(results)

    popping(rv,ascv,descv,constv, vv,vTime)
    plotting(rv,ascv,descv,constv, vv,vTime, "sS")

    deletions(rv,ascv,descv,constv,vTime)

    ################### for ms ###################
    rv = []
    ascv = []
    descv = []
    constv = []
    vv = []
    vTime = []
    mysort(r, vTime, rv, ascv, descv, constv, vv, mS)
    
    print("end of this iteration \n")
    #print(results)

    popping(rv,ascv,descv,constv, vv,vTime)
    plotting(rv,ascv,descv,constv, vv,vTime, "mS")

    deletions(rv,ascv,descv,constv,vTime)

    plot.show()
    exit()
if __name__ == "__main__":
    
    thread = threading.Thread(target=main) 
    thread.start()
    exit()
    #main()
