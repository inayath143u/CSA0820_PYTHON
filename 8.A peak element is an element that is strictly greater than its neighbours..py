def find_peak_element(nums):
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[n - 1] > nums[n - 2]:
        return n - 1
    
    for i in range(1, n - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i
    return -1

# Example usage
nums = [1, 2, 3, 1]
output = find_peak_element(nums)
print(output)  # Output: 2
