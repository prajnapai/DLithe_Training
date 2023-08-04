
input_str = input()
arr_shift = list(map(int,input().split()))

def shifting_letters(s, arr_shifts):
    shifts = [0] * len(arr_shifts)
    shifts[-1] = arr_shifts[-1] % 26 

    # Calculate cumulative shifts for each position in the shifts array
    for i in range(len(arr_shifts) - 2, -1, -1):
        shifts[i] = (shifts[i + 1] + arr_shifts[i]) % 26

    result = ""
    for i, char in enumerate(s):
        shift = shifts[i]
        shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        result += shifted_char

    return result

print(shifting_letters(input_str, arr_shift)) 

