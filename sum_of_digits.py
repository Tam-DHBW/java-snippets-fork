def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    return n % 10 + sum_of_digits(n // 10)  # Recursive call

print(sum_of_digits(1234))  # Output: 10 (1+2+3+4)
