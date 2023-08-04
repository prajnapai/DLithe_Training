def largest_continuous_sequence(arr):
    sum_to_index = {0: -1}
    max_length = 0
    end_index = -1

    current_sum = 0
    for i, num in enumerate(arr):
        current_sum += num

        if current_sum in sum_to_index:
            length = i - sum_to_index[current_sum]
            if length > max_length:
                max_length = length
                end_index = i

        else:
            sum_to_index[current_sum] = i

    if end_index != -1:
        start_index = end_index - max_length + 1
        return arr[start_index:end_index + 1]

    return []

arr = list(map(int, input().split()))
result = largest_continuous_sequence(arr)
print(result)
