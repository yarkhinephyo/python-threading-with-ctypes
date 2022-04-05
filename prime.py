from typing import List

def is_prime(num: int):
    for i in range(2, int(num**(0.5))):
        if num % i == 0:
            return 1
    return 0

def num_primes(num_list: List[int]):
    count = 0
    for num in num_list:
        count += is_prime(num)
    return count
