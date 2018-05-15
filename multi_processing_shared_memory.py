import multiprocessing

def calc_square(array_1, result, v):            # Accept the variable v, which is equals to zero, and this can be changed in the method.
    v.value = 10.10                             # If this will be implemented after the for there is going to be an error. ONLY excactly after the def.
    for id, number in enumerate(array_1):
        result[id] = number*number

if __name__ == "__main__":

    array = [18, 92, 126, 655, 989, 1002]  # Random given numbers from user or a txt or other file.

    """create a shared memory as an array. The indicator 'i' means that I am going
    to send integers and the second value has the name of the array that I
    want to pass into the process """
    result_of_multiprocessing = multiprocessing.Array('i',len(array))

    """Creation of a variable to be shared between the processes"""
    value_of_multiprocessing = multiprocessing.Value('d', 0.0)          # Creates a variable with type of double and gives a first value for the variable.

    # Create a process which focus on calc_square function and sending the array and two variables (result_of_multiprocessing & value_of_multiprocessing).
    process_01 = multiprocessing.Process(target=calc_square, args=(array, result_of_multiprocessing, value_of_multiprocessing))

    process_01.start()      # Process beings
    process_01.join()       # Process join (not useful for one process, but for an ideal project with multiple processes this is crucial!)

    print(value_of_multiprocessing.value) # Print the value which changed in the calc_square method, using the .value attribute
