import time
import threading
import os

arr = [2, 3, 4, 5]


def square(numbers):
    for n in numbers:
        time.sleep(2)
        print('Square : {0}, ProcessID : {1}'.format(n*n, os.getpid()))


def cube(numbers):
    for n in numbers:
        time.sleep(2)
        print('Cube : {0}, ProcessID : {1}'.format(n*n*n, os.getpid()))


print('Main process Id : {}'.format(os.getpid()))
t = time.time()
t1 = threading.Thread(target=square, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print(time.time() - t)
