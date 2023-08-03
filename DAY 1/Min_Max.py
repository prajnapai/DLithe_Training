numbers = list(map(int, input().strip().split()))
minimum = numbers[0]
maximum = numbers[0]
for i in numbers:
    if i < minimum:
        minimum = i
    else:
        maximum = i
print("Minimum = ", minimum,"\nMaximum = ", maximum)

