def fib(n):
    if Memo[n] is None:
        Memo[n] = fib(n-1) + fib(n-2)
    return Memo[n]

n = int(input())
Memo = [None for _ in range(n+1)]
Memo[0], Memo[1] = 1, 1
print(fib(n))