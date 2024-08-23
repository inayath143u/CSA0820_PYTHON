def sort_and_replace_negatives(arr):
    average = sum(arr) / len(arr) if arr else 0
    arr = [average if x < 0 else x for x in arr]
    arr.sort()
    return arr
numbers = [3, -1, 4, -2, 5]
sorted_numbers = sort_and_replace_negatives(numbers)
print(sorted_numbers)
