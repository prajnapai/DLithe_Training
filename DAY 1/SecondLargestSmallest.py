numbers = list(map(int, input().strip().split()))
numbers.sort()
print(numbers[1])
print(numbers[len(numbers) - 2])