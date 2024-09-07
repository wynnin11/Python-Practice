def fib(n):
    if n <=2:
        return 1
    return fib(n-1) +fib(n-2)

def fibmemo(n,memo={}):
    if n<=2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibmemo(n - 1, memo) + fibmemo(n - 2, memo)
    return memo[n]
print(fibmemo(50))
