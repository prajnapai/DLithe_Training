arr = list(map(int, input().split()))
k = int(input())
arr_set = set(arr)

for num in arr_set:
    complement = k - num
    if complement in arr_set:
        print(num, complement)
else:
    print("None")