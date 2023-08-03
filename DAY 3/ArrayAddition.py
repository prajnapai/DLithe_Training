# #Array Addition
n1 = int(input())
n2 = int(input())

array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
 
number1 = int(''.join(map(str, array1)))
number2 = int(''.join(map(str, array2)))

result = number1 + number2

result_array = [int(digit) for digit in str(result)]

print(result_array)
