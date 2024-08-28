

import sys
import time

def fib_list(max):
    numbers = []
    a, b = 0, 1
    while len(numbers) < max:
        numbers.append(b)
        a, b = b, a + b
    return numbers

def fib_gen(max):
    a, b = 0, 1
    count = 0
    while count <= max:
        a, b = b, a + b
        yield b
        count += 1

# Measuring Memory Usage
list_example = [i for i in range(10000)]
print("Memory occupied by the list:", sys.getsizeof(list_example), "bytes")

generator_example = (i for i in range(10000))
print("Memory occupied by the generator:", sys.getsizeof(generator_example), "bytes")

# Performance Comparison
list_start_time = time.time()
sum([i for i in range(9000000)])
list_stop_time = time.time() - list_start_time

generator_start_time = time.time()
sum((i for i in range(9000000)))
generator_stop_time = time.time() - generator_start_time

print("List processing time:", list_stop_time, "seconds")
print("Generator processing time:", generator_stop_time, "seconds")
