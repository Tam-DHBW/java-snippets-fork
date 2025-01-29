def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers.")
        return None
    else:
        print(f"The result is {result}")
        return result

divide(10, 2)  # The result is 5.0
divide(10, 0)  # Error: Cannot divide by zero.
divide(10, 'a')  # Error: Both inputs must be numbers.
