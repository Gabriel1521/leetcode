#QuickSort
def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j],arr[i]
    arr[high], arr[i+1] = arr[i+1],arr[high]
    return (i+1)

def quickSort(arr,low,high):
    if low <= high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)


def main():
    arr = [10, 7, 8, 9, 1, 5]
    print("Before ",arr)
    n = len(arr)
    quickSort(arr,0,n-1)
    print ("Sorted array is:",arr)


if __name__ == '__main__':
    main()

#MergeSort

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k] = L[i]
                i+=1
                k+=1
            else:
                arr[k] = R[j]
                j+=1
                k+=1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1


# Bubble Sort

# Python program for implementation of Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),


# Insertion Sort

def insertion_sort(arr, n):
    for i in range(1,n):
        element = arr[i]
        j = i-1
        while j>= 0 and arr[j] > element:
            arr[j+1] = arr[j]
            j -= 1
        arr[j] = element

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    insertion_sort(arr)
    print(arr)


# Selection Sort

# Python program for implementation of Selection
# Sort
import sys
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

# Driver code to test above
print ("Sorted array")
for i in range(len(A)):
    print("%d" %A[i]),


# Heap Sort

def big_endian(arr, start, end):
   root = start
   while True:
       child = root * 2 + 1   # 左孩子
       if child > end:        # 孩子比最后一个节点还大 也就意味着最后一个叶子节点了 就得跳出去一次循环已经调整完毕
           break
       if child + 1 <= end and arr[child] < arr[child + 1]:   # 为了始终让其跟子元素的较大值比较 如果右边大就左换右，左边大的话就默认
           child += 1
       if arr[root] < arr[child]:     # 父节点小于子节点直接换位置 同时坐标也得换这样下次循环可以准确判断是否为最底层是不是调整完毕
           arr[root], arr[child] = arr[child], arr[root]
           root = child
       else:                            # 父子节点顺序正常 直接过
           break


def heap_sort(arr):
   # 无序区大根堆排序
   first = len(arr) // 2 - 1
   for start in range(first, -1, -1):   # 从下到上，从右到左对每个节点进调整 循环得到非叶子节点
       big_endian(arr, start, len(arr) - 1)  # 去调整所有的节点
   for end in range(len(arr) - 1, 0, -1):
       arr[0], arr[end] = arr[end], arr[0]   # 顶部尾部互换位置
       big_endian(arr, 0, end - 1)          # 重新调整子节点的顺序  从顶开始调整
   return arr

def max_heap(arr, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and arr[child] < arr[child+1]:
            child += 1
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            break

def heap_sort(arr):
    first = len(arr)//2 - 1
    for start in range(first,-1,-1):
        max_heap(arr,start,len(arr)-1)
    for end in range(len(arr)-1,0,-1):
        arr[0], arr[end] = arr[end], arr[0]
        max_heap(arr,0,end-1)
    return arr


def main():
   l = [3, 1, 4, 9, 6, 7, 5, 8, 2, 10]
   print(heap_sort(l))  # 原地排序

if __name__ == "__main__":
   main()
