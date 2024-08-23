def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_non_composite_numbers(arr):
    return [num for num in arr if is_prime(num)]

array_of_elements = {26, 28, 47, 26, 43, 51, 29}
non_composite_numbers = find_non_composite_numbers(array_of_elements)

print("Prime numbers in Array elements =", non_composite_numbers)
