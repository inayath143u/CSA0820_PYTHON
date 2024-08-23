def find_mth_max_nth_min(arr, m, n):
    arr_sorted = sorted(arr)
    mth_max = arr_sorted[-m]
    nth_min = arr_sorted[n - 1]
    
    sum_result = mth_max + nth_min
    difference_result = mth_max - nth_min
    product_result = mth_max * nth_min
    
    return mth_max, nth_min, sum_result, difference_result, product_result

# Sample Input
array_of_elements = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

# Function Call
mth_max, nth_min, sum_result, difference_result, product_result = find_mth_max_nth_min(array_of_elements, M, N)

# Sample Output
print(f"{M}st Maximum Number = {mth_max} {N}rd Minimum Number = {nth_min} Sum = {sum_result}")
print(f"Difference = {difference_result}")
print(f"Product = {product_result}")
