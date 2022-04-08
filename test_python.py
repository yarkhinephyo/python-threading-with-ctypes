from prime import num_primes

MAX_NUM = 1000000
num_list = list(range(MAX_NUM))

def timeit_function():
    return num_primes(num_list)

print(f"Primes: {timeit_function()}")
