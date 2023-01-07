#! /usr/bin/env python3
from tkinter import *
from tkinter import ttk
import random
import time


def randomize(lines,canv,w,ind):
    ind.pack(side = RIGHT)
    w.update()
    heights = list()
    init = 480
    for _ in range(110):
        heights.append(init)
        init-=4
    
    for line in lines:
        new = random.choice(heights)
        heights.remove(new)
        x0, y0, x1, y1 = canv.coords(line)
        canv.coords(line,x0, new, x1, y1)
        canv.itemconfigure(line,outline = '#69ffd2',fill = '#69ffd2')
        w.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(line,outline = '#88aff7',fill = 'black')
        w.update_idletasks()
    w.update()
    ind.pack_forget()

def reset(lines,canv,root,ind):
    ind.pack(side = RIGHT)
    root.update()
    x1,x2,y1 = 15,17,480
    for line in lines:
        canv.coords(line,x1,y1,x2,500)
        canv.itemconfigure(line,outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(line,outline = '#88aff7',fill = 'black')
        root.update_idletasks()

        x1+=5  ; x2+=5 ; y1-=4
    ind.pack_forget() 
    root.update()

#def mergesort()

def BubbleSort(lines,canv,root,l,r):
    for i in range(len(lines)-1):
        for j in range(0,len(lines)-i-1):
            canv.itemconfigure(lines[j],outline = '#69ffd2',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.001)
            canv.itemconfigure(lines[j],outline = '#88aff7',fill = 'black')
            c1 = canv.coords(lines[j])
            c2 = canv.coords(lines[j+1])
            x0,y0,x1,y1 = c1
            x2,y2,x3,y3 = c2
            if c1[1] < c2[1]:
                canv.coords(lines[j],x0,y2,x1,y1)
                canv.coords(lines[j+1],x2,y0,x3,y3)
            root.update_idletasks()

def SelectionSort(lines,canv,root,l,r):
    for i in range(len(lines)-1):
        mn = i
        for j in range(i+1,len(lines)):
            canv.itemconfigure(lines[j],outline = '#69ffd2',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.001)
            canv.itemconfigure(lines[j],outline = '#88aff7',fill = 'black')
            c1 = canv.coords(lines[j])
            c2 = canv.coords(lines[mn])
            x0,y0,x1,y1 = c1
            x2,y2,x3,y3 = c2
            if c1[1] > c2[1]:
                mn = j
            root.update_idletasks()
        x0,y0,x1,y1 = canv.coords(lines[i])
        x2,y2,x3,y3 = canv.coords(lines[mn])
        canv.coords(lines[i],x0,y2,x1,y1)
        canv.coords(lines[mn],x2,y0,x3,y3)
        root.update_idletasks()


def InsertionSort(lines,canv,root,l,r):
    for i in range(1,len(lines)):
        key = canv.coords(lines[i])[1]
        j = i-1
        while j >= 0 and  key > canv.coords(lines[j])[1]:
            canv.itemconfigure(lines[j+1],outline = '#69ffd2',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.003)
            canv.itemconfigure(lines[j+1],outline = '#88aff7',fill = 'black')
            
            x2,y2,x3,y3 = canv.coords(lines[j+1])
            x0,y0,x1,y1 = canv.coords(lines[j])
            canv.coords(lines[j+1],x2,y0,x3,y3)
            
            j-=1
            root.update_idletasks()

        x2,y2,x3,y3 = canv.coords(lines[j+1]) 
        canv.coords(lines[j+1],x2,key,x3,y3)
        root.update_idletasks()

def CycleSort(lines,canv,root,l,r):
    # loop from the beginning of the array to the second to last item
    for currentIndex in range(0, r - 1):
        # save the value of the item at the currentIndex
        item = canv.coords(lines[currentIndex])[1]

        currentIndexCopy = currentIndex;
        # loop through all indexes that proceed the currentIndex
        for i in range(currentIndex + 1, r):
            canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.0005)
            canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')
            root.update_idletasks()
            if canv.coords(lines[i])[1] > item: currentIndexCopy += 1
            i+=1

        # if currentIndexCopy has not changed, the item at the currentIndex is already in the correct currentIndexCopy
        if currentIndexCopy == currentIndex:
            currentIndex+=1
            continue
        
        while item == canv.coords(lines[currentIndexCopy]): currentIndexCopy += 1

        # swap
        x0,y0,x1,y1 = canv.coords(lines[currentIndexCopy])
        canv.coords(lines[currentIndexCopy],x0,item,x1,y1)
        item = y0

        # repeat above steps as long as we can find values to swap
        while currentIndexCopy != currentIndex:

            currentIndexCopy = currentIndex
            # loop through all indexes that proceed the currentIndex
            i = currentIndex + 1
            while i < r:
                canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
                root.update_idletasks()
                time.sleep(0.0005)
                canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')
                root.update_idletasks()
                if canv.coords(lines[i])[1] > item: currentIndexCopy += 1
                i += 1

            while item == canv.coords(lines[currentIndexCopy]): currentIndexCopy += 1

            # swap
            x0,y0,x1,y1 = canv.coords(lines[currentIndexCopy])
            canv.coords(lines[currentIndexCopy],x0,item,x1,y1)
            item = y0

        currentIndex += 1

def MergeSort(lines,canv,root,l,r):
    

    if r-l<=1: return
    
    mid = (l+r)//2

    
    MergeSort(lines,canv,root,l,mid)
    MergeSort(lines,canv,root,mid,r) 
    left = [canv.coords(lines[i])[1] for i in range(l,mid)]
    
    if left:    
        canv.itemconfigure(left[-1],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(left[-1],outline = '#88aff7',fill = 'black')
    
    right = [canv.coords(lines[i])[1] for i in range(mid,r)]
    
    
    if right:
        canv.itemconfigure(right[-1],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(right[-1],outline = '#88aff7',fill = 'black')

    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        canv.itemconfigure(lines[k],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(lines[k],outline = '#88aff7',fill = 'black')

        if left[i] >= right[j]:
            x1,y1,x2,y2 = canv.coords(lines[k])
            canv.coords(lines[k],x1,left[i],x2,y2)
            i+=1
        else:
            x1,y1,x2,y2 = canv.coords(lines[k])
            canv.coords(lines[k],x1,right[j],x2,y2)
            j+=1
        k+=1
    while i < len(left):
        canv.itemconfigure(lines[k],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(lines[k],outline = '#88aff7',fill = 'black')
        
        x1,y1,x2,y2 = canv.coords(lines[k])
        canv.coords(lines[k],x1,left[i],x2,y2)
        i+=1 ; k+=1
    while j < len(right):
        canv.itemconfigure(lines[k],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(lines[k],outline = '#88aff7',fill = 'black')
        
        x1,y1,x2,y2 = canv.coords(lines[k])
        canv.coords(lines[k],x1,right[j],x2,y2)
        j+=1 ; k+=1




def CountingSort(lines,canv,root,l,r):
    for line in lines:
        canv.itemconfigure(line,outline = 'yellow',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.015)
        canv.itemconfigure(line,outline = '#88aff7',fill = 'black')
    x1,x2,y1 = 15,17,480
    
    for line in lines:
        canv.itemconfigure(line,outline = '#69ffd2',fill = '#69ffd2')
        canv.coords(line,x1,y1,x2,500)
        time.sleep(0.015)
        root.update_idletasks()
        canv.itemconfigure(line,outline = '#88aff7',fill = 'black')
        x1+=5  ; x2+=5 ; y1-=4

def helper(lines,canv,root,place):
    
    n = len(lines)
    output = [0] * n
    count = [0] * 10

    for i in range(0, n):
        index = int(canv.coords(lines[i])[1]) // place
        count[index % 10] += 1
    for i in range(1,10):
        count[i]+= count[i-1]

    for i in range(n-1,-1,-1):
        index = int(canv.coords(lines[i])[1]) // place
        output[count[index % 10]-1] = int(canv.coords(lines[i])[1])
        count[index % 10] -= 1

    for i in range(n-1,-1,-1):
        x0,y0,x1,y1 = canv.coords(lines[i])
        canv.coords(lines[i],x0,output[i],x1,y1)
        canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.008)
        canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')

def RadixSort(lines,canv,root,l,r):
    mx = 480
    place = 1
    while mx //place > 0:
        for line in lines:
            canv.itemconfigure(line,outline = 'yellow',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.005)
            canv.itemconfigure(line,outline = '#88aff7',fill = 'black')
        helper(lines,canv,root,place)
        place*=10
    r-=1

    while l<r:
        x0,y0,x1,y1 = canv.coords(lines[l])
        x2,y2,x3,y3 = canv.coords(lines[r])
        canv.coords(lines[l],x0,y2,x1,y1)
        canv.coords(lines[r],x2,y0,x3,y3)

        canv.itemconfigure(lines[l],outline = '#69ffd2',fill = '#69ffd2')
        canv.itemconfigure(lines[r],outline = '#69ffd2',fill = '#69ffd2')
        
        root.update_idletasks()
        time.sleep(0.005)
        
        canv.itemconfigure(lines[l],outline = '#88aff7',fill = 'black')
        canv.itemconfigure(lines[r],outline = '#88aff7',fill = 'black')
        root.update_idletasks()
        
        l+=1 ; r-=1


def heapify(lines,canv,root,n,i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
    canv.itemconfigure(lines[largest],outline = '#69ffd2',fill = '#69ffd2')
    root.update_idletasks()
    time.sleep(0.01)
    canv.itemconfigure(lines[largest],outline = '#88aff7',fill = 'black')
    root.update_idletasks()

    # See if left child of root exists and is
    # greater than root

    if l < n and canv.coords(lines[i])[1] > canv.coords(lines[l])[1]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and canv.coords(lines[largest])[1] > canv.coords(lines[r])[1]:
        largest = r

    # Change root, if needed

    if largest != i:
        #(arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
    # Heapify the root.
        x0,y0,x1,y1 = canv.coords(lines[i])
        x2,y2,x3,y3 = canv.coords(lines[largest])
        canv.coords(lines[i],x0,y2,x1,y1)
        canv.coords(lines[largest],x2,y0,x3,y3)
        root.update_idletasks()
        heapify(lines,canv,root,n,largest)



def HeapSort(lines,canv,root,l,r):
    n = len(lines)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lines,canv,root,n, i)

# One by one extract elements

    for i in range(n - 1, 0, -1):

        x0,y0,x1,y1 = canv.coords(lines[i])
        x2,y2,x3,y3 = canv.coords(lines[0])
        canv.coords(lines[i],x0,y2,x1,y1)
        canv.coords(lines[0],x2,y0,x3,y3)
    #(arr[i], arr[0]) = (arr[0], arr[i])  # swap

        heapify(lines,canv,root,i, 0)

def partition(lines,canv,root,l,r):

    # choose the rightmost element as pivot
    pivot = canv.coords(lines[r])[1]
    # pointer for greater element
    i = l - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(l, r):
        canv.itemconfigure(lines[j],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.01)
        canv.itemconfigure(lines[j],outline = '#88aff7',fill = 'black')
        if canv.coords(lines[j])[1] > pivot:
        # If element smaller than pivot is found
        # swap it with the greater element pointed by i
            i = i + 1
            x0,y0,x1,y1 = canv.coords(lines[i])
            x2,y2,x3,y3 = canv.coords(lines[j])
            canv.coords(lines[i],x0,y2,x1,y1)
            canv.coords(lines[j],x2,y0,x3,y3)
        root.update_idletasks()
        

    # Swap the pivot element with the greater element specified by i
    x0,y0,x1,y1 = canv.coords(lines[i+1])
    x2,y2,x3,y3 = canv.coords(lines[r])
    canv.coords(lines[i+1],x0,y2,x1,y1)
    canv.coords(lines[r],x2,y0,x3,y3)
    canv.itemconfigure(lines[r],outline = '#69ffd2',fill = '#69ffd2')
    root.update_idletasks()
    time.sleep(0.005)
    canv.itemconfigure(lines[r],outline = '#88aff7',fill = 'black')
    root.update_idletasks()

    return i + 1

def QuickSort(lines,canv,root,l,r):
    if l < r:
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
        pi = partition(lines,canv,root,l,r)

        # Recursive call on the left of pivot
        QuickSort(lines,canv,root,l,pi-1)

        # Recursive call on the right of pivot
        QuickSort(lines,canv,root,pi+1,r)
def GnomeSort(lines,canv,root,l,r):
    i = 0
    while i < r:
        canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.001)
        canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')
        root.update_idletasks()

        if i == 0 or canv.coords(lines[i])[1] <= canv.coords(lines[i-1])[1]:
            i+=1
        else:
            x0,y0,x1,y1 = canv.coords(lines[i-1])
            x2,y2,x3,y3 = canv.coords(lines[i])
            canv.coords(lines[i-1],x0,y2,x1,y1)
            canv.coords(lines[i],x2,y0,x3,y3)
            i-=1
def ShellSort(lines,canv,root,l,r):
    # code here
    gap=r//2


    while gap>0:
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<r:
            i=j-gap # This will keep help in maintain gap value

            while i>=0:
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
                root.update_idletasks()
                time.sleep(0.008)
                canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')                
                root.update_idletasks()
                if canv.coords(lines[i+gap])[1]<canv.coords(lines[i])[1]:
                    break
                else:
                    x0,y0,x1,y1 = canv.coords(lines[i+gap])
                    x2,y2,x3,y3 = canv.coords(lines[i])
                    canv.coords(lines[i+gap],x0,y2,x1,y1)
                    canv.coords(lines[i],x2,y0,x3,y3)
                root.update()
                i=i-gap # To check left side also
                # If the element present is greater than current element
            j+=1
        gap=gap//2
def CocktailSort(lines,canv,root,l,r):
    n = r
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):

# reset the swapped flag on entering the loop,
# because it might be true from a previous
# iteration.
        swapped = False

# loop from left to right same as the bubble
# sort
        for i in range(start, end):
            
            canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.0005)
            canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')                
            root.update_idletasks()
            
            if canv.coords(lines[i])[1]<canv.coords(lines[i+1])[1]:
                x0,y0,x1,y1 = canv.coords(lines[i+1])
                x2,y2,x3,y3 = canv.coords(lines[i])
                canv.coords(lines[i+1],x0,y2,x1,y1)
                canv.coords(lines[i],x2,y0,x3,y3)
                swapped = True

# if nothing moved, then array is sorted.
        if (swapped == False):
            break

# otherwise, reset the swapped flag so that it
# can be used in the next stage
        swapped = False

# move the end point back by one, because
# item at the end is in its rightful spot
        end = end-1

# from right to left, doing the same
# comparison as in the previous stage
        for i in range(end-1, start-1, -1):
            canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.0005)
            canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')                
            root.update_idletasks()
            
            if canv.coords(lines[i])[1]<canv.coords(lines[i+1])[1]:
                x0,y0,x1,y1 = canv.coords(lines[i+1])
                x2,y2,x3,y3 = canv.coords(lines[i])
                canv.coords(lines[i+1],x0,y2,x1,y1)
                canv.coords(lines[i],x2,y0,x3,y3)
                swapped = True

# increase the starting point, because
# the last stage would have moved the next
# smallest number to its rightful spot.
        start = start + 1
def getNextGap(gap):

# Shrink gap by Shrink factor
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
def CombSort(lines,canv,root,l,r):
    n = r

# Initialize gap
    gap = n

    # Initialize swapped as true to make sure that
    # loop runs
    swapped = True

    # Keep running while gap is more than 1 and last
    # iteration caused a swap
    while gap !=1 or swapped:
        

    # Find next gap
        gap = getNextGap(gap)

        # Initialize swapped as false so that we can
        # check if swap happened or not
        swapped = False

        # Compare all elements with current gap
        for i in range(0, n-gap):
            canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
            root.update_idletasks()
            time.sleep(0.002)
            canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')                
            root.update_idletasks()

            if canv.coords(lines[i])[1]<canv.coords(lines[i+gap])[1]:
                x0,y0,x1,y1 = canv.coords(lines[i+gap])
                x2,y2,x3,y3 = canv.coords(lines[i])
                canv.coords(lines[i+gap],x0,y2,x1,y1)
                canv.coords(lines[i],x2,y0,x3,y3)
                swapped = True
def flip(lines, i,canv,root):
    start = 0
    while start < i:
        canv.itemconfigure(lines[i],outline = '#69ffd2',fill = '#69ffd2')
        canv.itemconfigure(lines[start],outline = '#69ffd2',fill = '#69ffd2')
        root.update_idletasks()
        time.sleep(0.0005)
        canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')                
        canv.itemconfigure(lines[start],outline = '#88aff7',fill = 'black')                

        x0,y0,x1,y1 = canv.coords(lines[start])
        x2,y2,x3,y3 = canv.coords(lines[i])
        canv.coords(lines[start],x0,y2,x1,y1)
        canv.coords(lines[i],x2,y0,x3,y3)
        root.update_idletasks()

        start += 1
        i -= 1
def findMax(lines, n,canv,root):
    mi = 0
    for i in range(0,n):
        canv.itemconfigure(lines[i],outline = 'yellow',fill = 'yellow')
        root.update_idletasks()
        time.sleep(0.0005)
        canv.itemconfigure(lines[i],outline = '#88aff7',fill = 'black')
        root.update()     
        if canv.coords(lines[i])[1] < canv.coords(lines[mi])[1]:
            mi = i
    return mi


def PancakeSort(lines,canv,root,l,r):
    # Start from the complete
# array and one by one
# reduce current size
# by one
    curr_size = r
    while curr_size > 1:
# Find index of the maximum
# element in 
# arr[0..curr_size-1]
        mi = findMax(lines, curr_size,canv,root)

# Move the maximum element
# to end of current array
# if it's not already at 
# the end
        if mi != curr_size-1:
# To move at the end, 
# first move maximum 
# number to beginning 
            flip(lines, mi,canv,root)

# Now move the maximum 
# number to end by
# reversing current array
            flip(lines, curr_size-1,canv,root)
        curr_size -= 1


def change_sort(choice,l):
    l['text'] = choice['text']

algos = {'Pancake Sort':PancakeSort,'Comb Sort':CombSort,'Shell Sort':ShellSort,'Cocktail Sort':CocktailSort,'Gnome Sort':GnomeSort,'Cycle Sort':CycleSort,'Radix Sort':RadixSort,'Bubble Sort':BubbleSort,'Heap Sort':HeapSort,'Merge Sort': MergeSort,'Quick Sort':QuickSort,'Insertion Sort': InsertionSort,'Selection Sort':SelectionSort,'Counting Sort':CountingSort}

def hide_list(event,f,d):
    f.place_forget()
    d.bind('<Button-1>',lambda event: show_list(event,f,d))

def show_list(event,f,d):
    f.place(x=328,y=38)
    d.bind('<Button-1>',lambda event: hide_list(event,f,d))

def pick_algo(curr_algo,lines,canv,root,ind):
    ind.pack(side = RIGHT)
    root.update()
    val = curr_algo['text']
    algos[val](lines,canv,root,0,len(lines) if val != 'Quick Sort' else len(lines)-1)
    ind.pack_forget()
    root.update()

def run():

    root = Tk()
    root.resizable(False,False)
    root.config(bg = '#06071a')
    root.geometry('580x603')
    root.title('Sorting VisualiZer')
    
    top_bar = Frame(master = root , bg = '#030414')
    top_bar.pack(side = TOP, fill=X,ipady=(10))


    window = Frame(master = root , bg = '#0c0d17')
    window.pack(side = TOP, fill=X)
    
    canv = Canvas(master = window , bg='#0c0d17',height=550, bd = 0 , highlightthickness=0 )
    canv.pack(side = TOP,fill=X,pady=(40,0))
    lines = []
    x1,x2,y1 = 15,17,480
    for i in range(110):
        lines.append(canv.create_rectangle(x1,y1,x2,500,fill = '#0b1173',outline='#88aff7'))
        x1+=5  ; x2+=5 ; y1-=4 
    shuffle_button = Button(master = top_bar , cursor="hand2",text='Shuffle',relief = FLAT,font=('',9) , bg = '#030414',fg ='white' )
    shuffle_button.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightcolor='#88aff7',highlightbackground='#88aff7',highlightthickness=1)
    shuffle_button.pack(side = LEFT,padx=(10,0))
    shuffle_button.config(command=lambda:randomize(lines,canv,root,ind2))


    reset_button = Button(master = top_bar , cursor="hand2",text='Reset',relief = FLAT,font=('',9) , bg = '#030414',fg ='white' )
    reset_button.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightcolor='#88aff7',highlightbackground='#88aff7',highlightthickness=1)
    reset_button.pack(side = LEFT,padx=(10,0))
    reset_button.config(command=lambda:reset(lines,canv,root,ind3))

    sort_button = Button(master = top_bar , cursor="hand2",text='Sort',relief = FLAT,font=('',9) , bg = '#030414',fg ='white' )
    sort_button.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightcolor='#88aff7',highlightbackground='#88aff7',highlightthickness=1)
    sort_button.pack(side = LEFT,padx=(10,0))
    sort_button.config(command=lambda:pick_algo(curr_algo,lines,canv,root,ind1))

    curr_algo = Label(master = top_bar ,text='Bubble Sort',width=13,relief = FLAT,font=('',9) , bg = '#030414',fg ='white' )
    curr_algo.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightcolor='#88aff7',highlightbackground='#88aff7',highlightthickness=1)

    ind1 = Label(master = top_bar ,text='Sorting..',width=13,relief = FLAT,font=('',9) , bg = '#030414',fg ='#88aff7' )
    ind1.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightthickness=0,bd = 0)

    ind2 = Label(master = top_bar ,text='Randomizing..',width=13,relief = FLAT,font=('',9) , bg = '#030414',fg ='#88aff7' )
    ind2.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightthickness=0,bd = 0)

    ind3 = Label(master = top_bar ,text='Resetting..',width=13,relief = FLAT,font=('',9) , bg = '#030414',fg ='#88aff7' )
    ind3.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightthickness=0,bd = 0)


    list_frame = Frame(master = root,bg = '#030414')
    
    names = ['Cycle Sort','Radix Sort','Gnome Sort','Shell Sort','Cocktail Sort','Comb Sort','Pancake Sort']
    r = 0
    for name in names:
        b = (Button(master = list_frame, cursor="hand2",text = name,relief = FLAT,font=('',9) , bg = '#030414',fg ='white',activebackground='#0c0d17',activeforeground='#88aff7',highlightcolor='#88aff7',highlightbackground='#88aff7',highlightthickness=1))
        b.grid(column=1,row=r,sticky=EW)
        b.config(command = lambda v = b:change_sort(v,curr_algo))
        r+=1
    
    names = ['Bubble Sort','Insertion Sort','Selection Sort','Merge Sort','Quick Sort','Heap Sort','Counting Sort']
    r = 0
    for name in names:
        b = (Button(master = list_frame, cursor="hand2",text = name,relief = FLAT,font=('',9) , bg = '#030414',fg ='white',activebackground='#0c0d17',activeforeground='#88aff7',highlightcolor='#88aff7',highlightbackground='#88aff7',highlightthickness=1))
        b.grid(column=0,row=r,sticky=EW)
        b.config(command = lambda v = b:change_sort(v,curr_algo))
        r+=1



    
    drop_down = Label(master = top_bar , cursor="hand2",text='⬇',relief = FLAT,font=('',9) , bg = '#030414',fg ='#88aff7' )
    drop_down.config(activebackground='#0c0d17',activeforeground='#88aff7',highlightcolor='#88aff7',highlightbackground='#88aff7',highlightthickness=1)
    drop_down.pack(side = RIGHT,padx=(0,40),ipady=4,ipadx=4)
    drop_down.bind('<Button-1>',lambda event: show_list(event,list_frame,drop_down))

    curr_algo.pack(side = RIGHT,padx=(0),ipady=4,anchor=W)
    
    root.mainloop() 


if __name__ == '__main__':
    run()