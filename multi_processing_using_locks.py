import time
import multiprocessing


""" Description at the end of the code !! """

def buy(salary, lock):
    for i in range(10):
        time.sleep(0.01)
        lock.acquire()  # critical section starts hear
        salary.value = salary.value + 1
        lock.release()  # critical section ends hear

def sell(salary, lock):
    for i in range(10):
        time.sleep(0.01)
        lock.acquire() # critical section starts hear
        salary.value = salary.value - 1
        lock.release() # critical section ends hear

if __name__ == "__main__":
    salary = multiprocessing.Value('i', 1000)                              # Let's say that the salary is 1000 euros and with these I want to buy/sell stocks.
    lock = multiprocessing.Lock()                                          # Enables the multi-processing to be executed in order.
    starting_time = time.time()                                            # Keeping the starting time.
    buy_move = multiprocessing.Process(target=buy, args=(salary, lock))    # Declaring the buy process (sending salary and lock into the function).
    sell_move = multiprocessing.Process(target=sell, args=(salary, lock))  # Declaring the sell process (sending salary and lock into the function).

    buy_move.start()        # Start the buy process
    sell_move.start()       # Start the sell process

    buy_move.join()         # Helps to make coordinated switches between the processes
    sell_move.join()

    print(salary.value)     # Printing the last amount of the salary [ It has to be 1000 because that is what I wanted to do.]
    print("Estimated time: ", time.time()-starting_time)

    """

    Using the lock function to make the functions of buy and sell to run the one after the other without delays. Without the lock,
    the salary at the end of the execution, change values. It may be 998, 1001, 999 and more. This is because some times the threads
    are having a delay. With the usage of lock, I make them executable in a coordinated way, without delays. And as a result if the starting
    salary of mine is 1000 at the end of the project it has to be 1000 again.


