#Insertion Sort

arr = list(map(int,input().strip().split()))
length = len(arr)

def InsertionSort(arr):
    for i in range(1,length):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
InsertionSort(arr)
print(*arr)