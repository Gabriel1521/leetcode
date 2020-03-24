#Quick sort

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

# Merge sort

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    arr = [10, 7, 8, 9, 1, 5]
    print("Before ",arr)
    n = len(arr)
    quickSort(arr,0,n-1)
    print ("Sorted array is:",arr)


if __name__ == '__main__':
    main()
