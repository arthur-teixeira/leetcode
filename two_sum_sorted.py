def twoSum(numbers, target):
    high = len(numbers) - 1
    low = 0
    while high >= low:
        sum = numbers[high] + numbers[low]
        if sum == target:
            return [low, high]
        elif sum > target:
            high -= 1
        elif sum < target:
            low += 1


print(twoSum([2, 7, 11, 15], 9))
