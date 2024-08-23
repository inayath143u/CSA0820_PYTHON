def smallerNumbersThanCurrent(nums):
    return [sum(num < x for num in nums) for x in nums]

# Example usage
nums = [8, 1, 2, 2, 3]
output = smallerNumbersThanCurrent(nums)
print(output)  # Output: [4, 0, 1, 1, 3]
