from ctypes import *
from timeit import default_timer as timer

lib = CDLL("./libprime.so")
lib.num_primes.restype = c_int32
lib.num_primes.argtypes = [c_int32, POINTER(c_int32)]

MAX_NUM = 2000000
num_list = list(range(MAX_NUM))

start = timer()
count = lib.num_primes(MAX_NUM, (c_int32 * MAX_NUM)(*num_list))
end = timer()

print(f"Primes: {count}\tTime: {end - start:.5f}")
