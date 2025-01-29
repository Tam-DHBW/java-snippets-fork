def fibonacci(n):
    """Return the first n Fibonacci numbers as a list."""
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(10))  # Output: first 10 Fibonacci numbers
