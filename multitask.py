import time

arr = [2, 3, 4, 5]


def square(numbers):
    for n in numbers:
        time.sleep(2)
        print('Square : ' + str(n*n))


def cube(numbers):
    for n in numbers:
        time.sleep(2)
        print('Cube : ' + str(n*n*n))


t = time.time()
square(arr)
cube(arr)
print(time.time() - t)
