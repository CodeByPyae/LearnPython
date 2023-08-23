# Recursive function

# Example 1 - Factorial of a non-negative interger
# x! = x * (x - 1)!
def fact(x):
    if x > 1 :
        return x * fact(x - 1)
    else :
        return 1
    
# Example 2 - Fibonacci sequence
# (n - 1) + (n - 2)
def fibonacci(n):
    if n <= 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example 3 - Calculate the sum of all elements in an array
def arraysum(arr, index = 0):
    if index >= len(arr) :
        return 0
    else :
        return arr[index] + arraysum(arr, index + 1)
    
x = int(input("Enter number: "))

print(f"Factorial result - {x}! is {fact(x)}.")
print(f"Fibonacci of {x} is {fibonacci(x)}")

arr = [2,4,6,8,10,12,14]
print(f"Arrary sum of {arr} is {arraysum(arr)}")