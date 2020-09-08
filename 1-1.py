def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n-1)


print(fib1(10))
