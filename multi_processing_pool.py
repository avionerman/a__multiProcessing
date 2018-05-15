"""
With the pool i can use multiple CPUs to run the same program,
so it's going to run faster and quicker

It is actually a Map and Reduce. Map is when the CPUs GET the input data
and Reduce is when the CPUs GIVE back the output data
"""

from multiprocessing import Pool
import time

def pool(number):           # Just counting something that needs time, so to test the multi-processing,
    sum_total = 0
    for i in range(100000):
        sum_total += i*i*i
    return sum_total

if __name__ == "__main__":

    time_1 = time.time()    # Keep the starting time.

    pool_01 = Pool()                            # I can put 'processes=1 ,2 ,3 ..' to use as many as I want.
    result = pool_01.map(pool, range(1000))     # Declare the beginning of mapping with the function name [pool] and the data [range(1000)].
    pool_01.close()
    pool_01.join()                              # Will return ONLY if all the calculations done.


    result = []
    for i in range(1000):
        result.append(pool(i))

    print("Serial processing took: ", time.time()-time_1)
