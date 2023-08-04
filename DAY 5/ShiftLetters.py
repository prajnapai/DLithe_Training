#Shifting characters in a string

input_str = input()
arr_shift = list(map(int,input().split()))

def ShiftLetters(inp,arr_shift):
    shifted = ""
    for i,char in enumerate(inp):
        shift = arr_shift[i % len(arr_shift)]
        shift_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        shifted += shift_char
    return shifted

res = ShiftLetters(input_str,arr_shift)
print(res)

