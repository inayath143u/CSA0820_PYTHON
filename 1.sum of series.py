def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_factorials(N):
    total_sum = 0
    for i in range(1, N + 1):
        total_sum += factorial(i) / i
    return total_sum

# Sample input
N = 5
result = sum_of_factorials(N)
print(f"Sum={result}")
