def SelectionSort(n,arr):
    for i in range(n):
        min_index = i

        for j in range(i+1,n):
            if arr[j] < arr[min_index]:   #for descending order just change arr[j] > arr[min_index]
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr

n = int(input())
arr = list(map(int,input().split()))

result = SelectionSort(n,arr)
print(result)