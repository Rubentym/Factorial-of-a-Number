def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Calculate factorial of 5
result = factorial(5)
print("Factorial of 5:", result)
