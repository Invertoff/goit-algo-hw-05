def caching_fibonacci():
    # Creating an empty dict for cache.
    cache = {}   

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # If value already exists in cache, we return it.
        if n in cache:
            return cache[n]
        # If value is absent in cache, we calculate it with recursion.
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) 
        return cache[n]
    # Returning inner fibonacci function.
    return fibonacci

# Example of use
start_fib = caching_fibonacci()
print(start_fib(9))
print(start_fib(15))