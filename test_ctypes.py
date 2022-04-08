from ctypes import *

lib = CDLL("./libprime.so")
lib.num_primes.restype = c_int32
lib.num_primes.argtypes = [c_int32, POINTER(c_int32)]

MAX_NUM = 1000000
num_list = list(range(MAX_NUM))

def timeit_function():
    return lib.num_primes(MAX_NUM, (c_int32 * MAX_NUM)(*num_list))

print(f"Primes: {timeit_function()}")
