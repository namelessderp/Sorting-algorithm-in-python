#Bubble Sort

def BubbleSort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                arr[i-1],arr[i] = arr[i],arr[i-1]
                swap = True
    return arr

##arr = [1,5,3,6,9,10,4,2]
##print(BubbleSort(arr))

#Insertion Sort

def InsertionSort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
    return arr

##arr = [1,5,3,6,9,10,4,2]
##print(InsertionSort(arr))

def Partition(arr,first,last):
    pivot = arr[first]
    left = first+1
    right = last
    done = False
    while done == False:
        while left<=right and arr[left] < pivot:
            left+=1

        while left<= right and arr[right] > pivot:
            right-=1
        if left > right:
            done = True
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first],arr[right] = arr[right],arr[first]
    return right
             
    
    
def QuickSort(arr,first,last):
    if first<last:
        splitPoint = Partition(arr,first,last)
        QuickSort(arr,first,splitPoint -1) #left sub array
        QuickSort(arr,splitPoint+1, last) #right sub array
    return arr

arr = [1,5,3,6,9,10,4,2]
print(QuickSort(arr,0,len(arr)-1))#rmb -1

    
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        i,j,k =0,0,0 #left ptr,right ptr,sorted ptr
        MergeSort(left)
        MergeSort(right)

        while i <len(left) and j <len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1

        while i <len(left):
            arr[k] = left[i]
            i+=1
            k+=1

        while j <len(right):
            arr[k] = right[j]
            j+=1
            k+=1
    return arr

##arr = [1,5,3,6,9,10,4,2]
##print(MergeSort(arr))
