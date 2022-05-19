def isPalindrome(x):
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


isPalindrome(121)