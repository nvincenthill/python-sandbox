def fib(n):
    # returns a list containing the Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


f100 = fib(100)    # call it
print(f100)                # write the result

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
