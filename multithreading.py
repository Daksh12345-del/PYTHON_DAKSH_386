import threading
import time
from concurrent.futures import ThreadPoolExecutor
# Indicates some task being done 
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1=time.perf_counter()
#Normal code
# func(4)
# func(2)
# func(1)
time2=time.perf_counter()
print(f"Normal code time: {time2-time1}")

#Same code using threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()


time2=time.perf_counter()
print(f"Normal code time: {time2-time1}")

def pooling_demo():
    with ThreadPoolExecutor() as executor:
        future=executor.submit(func, 3)
        print(future.result())
        future=executor.submit(func, 2)
        print(future.result())
        future=executor.submit(func, 4)
        print(future.result())
pooling_demo()