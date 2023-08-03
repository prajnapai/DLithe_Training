length = int(input())
arr = list(map(int, input().strip().split()))

count = 1
maximum = arr[0]
for i in range(1,length):
    if arr[i] > maximum:
        count += 1
        maximum = arr[i]
print(count)
