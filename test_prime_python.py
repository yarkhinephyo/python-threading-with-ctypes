from prime import num_primes
from timeit import default_timer as timer

MAX_NUM = 2000000
num_list = list(range(MAX_NUM))

start = timer()
count = num_primes(num_list)
end = timer()

print(f"Primes: {count}\tTime: {end - start:.5f}")
