import multiprocessing
import math
import sys
import time

## increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

##function to compute factorials of a givem number 
def computer_factorial(num):
    print(f"computing factorial of {num}")
    result=math.factorial(num)
    print(f'factorial of {num} is { result}')
    return result
  
if __name__=="__main__":
    numbers=[5000,6000,700,8000]
    start_time=time.time()
    # create a pool of work processes
    with multiprocessing.Pool() as pool:
        results=pool.map(computer_factorial,numbers)
        end_time=time.time()
        print(f"results:{results}")
        print(f"time taken:{end_time-start_time} seconds")