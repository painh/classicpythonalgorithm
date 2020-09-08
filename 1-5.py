def fib5(n: int) -> int:
    if n == 0:
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        # last, next = next, last+next
        cur = next
        next = last + next
        last = cur
    return next


print(fib5(50))