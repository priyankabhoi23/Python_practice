# Reversing a Number using Recursion in Python
def reverse_digit(arr, l):
    for i in range(l):
        arr[i], arr[-1 * (i + 1)] = arr[-1 * (i + 1)], arr[i]
    return arr


num = 12345
arr = list(str(num))
arr = reverse_digit(arr, len(arr)//2)
s = ""
print(int(s.join(arr)))