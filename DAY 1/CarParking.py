row = int(input())
col = int(input())
sum = 0
m = 0
res= 0
for i in range(row):
    for j in range(col):
        sum += int(input())
    if sum > m:
        m = sum
        res = i + 1
    sum = 0
print(res)