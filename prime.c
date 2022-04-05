#include <stdio.h>
#include <math.h>

int is_prime(int num) {
    for (int i=2; i<(int)sqrt(num); i++) {
        if (num % i == 0)
            return 1;
    }
    return 0;
} 

int num_primes(int arrSize, int *numArr) {
    int count = 0;
    for (int i=0; i<arrSize; i++)
        count += is_prime(numArr[i]);
    return count;
}
