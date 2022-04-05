from ctypes import *
from timeit import default_timer as timer
import threading

lib = CDLL("./libprime.so")
lib.num_primes.restype = c_int32
lib.num_primes.argtypes = [c_int32, POINTER(c_int32)]

MAX_NUM = 2000000
NUM_THREADS = 4

# Prime counts per thread
count_list = [0 for _ in range(NUM_THREADS)]
# One list of numbers for each thread
num_list_list = []

# Split the list for multiple threads
for i in range(NUM_THREADS):
    num_list = list(range(i, MAX_NUM, NUM_THREADS))
    num_list_list.append(num_list)

# Function run by each thread
def thread_function(i, num_list, count_list):
    len_num_list = len(num_list)
    count_list[i] = lib.num_primes(len_num_list, (c_int32 * len_num_list)(*num_list))

start = timer()
threads = []
for i in range(NUM_THREADS):
    t = threading.Thread(target=thread_function, args=(i, num_list_list[i], count_list))
    t.start()
    threads.append(t)
for thread in threads:
    thread.join()
count = sum(count_list) # Combine counts from each thread
end = timer()

print(f"Primes: {count}\tTime: {end - start:.5f}")
