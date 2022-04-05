#include <stdio.h>
#include <math.h>
#include <pthread.h>
#include <stdlib.h>

#define NUM_THREADS 4

int is_prime(int num) {
    for (int i=2; i<(int)sqrt(num); i++) {
        if (num % i == 0)
            return 1;
    }
    return 0;
}

int *gArrSize = 0;
int *gNumArr = 0;
int countByThreads[NUM_THREADS] = { 0 };
pthread_t tids[NUM_THREADS] = { 0 };

// Function run by each thread
void *thread_function(void *vargp) {
    int offset = (*(int*) vargp);
    int count = 0;
    // Split the array items evenly across threads
    for (int i=offset; i < *gArrSize; i+=NUM_THREADS)
        count += is_prime(gNumArr[i]);
    countByThreads[offset] += count;
    free(vargp);
}

int num_primes(int arrSize, int *numArr) {
    gArrSize = &arrSize;
    gNumArr = numArr;
    for(int i=0; i < NUM_THREADS; i++) {
        int *offset = (int*) malloc(sizeof(int));
        *offset = i;
        if(pthread_create(&tids[i], NULL, thread_function, (void *) offset) == -1)
            exit(1);
    }
    int count = 0;
    for(int i=0; i < NUM_THREADS; i++) {
        if(pthread_join(tids[i], NULL) == -1)
            exit(1);
        // Combine counts from each thread
        count += countByThreads[i];
    }
    return count;
}
