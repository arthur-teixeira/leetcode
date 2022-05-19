from math import floor

# Naive O(n) time and O(n) space


def is_palindrome(x):
    arr = []
    arr.extend(str(x))
    high = len(arr) - 1
    low = 0
    while high >= low:
        if arr[low] != arr[high]:
            return False
        low += 1
        high -= 1
    return True

# Fastest solution time O(log10(n)) space O(1)


def is_palindrome_reversing_num(x: int) -> bool:
    tmp = x
    reversed_num = 0
    while tmp > 0:
        last_digit = tmp % 10
        reversed_num = reversed_num * 10 + last_digit
        tmp = tmp // 10
    return x == reversed_num


is_palindrome_reversing_num(12321)
