fibonacci = lambda n: n if n<=1 else fibonacci(n-1)+fibonacci(n-2)
n_terms = 10
fib_series = [fibonacci(i) for i in range(n_terms)]
print(fib_series)