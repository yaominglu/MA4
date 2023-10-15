import random
import math
import concurrent.futures
import time

def volume(args):
    n, d = args
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    points_2 = [list(map(lambda x: x**2, point)) for point in points]
    sum_p = [sum(point) for point in points_2]
    in_points = [x for x in sum_p if x <= 1]
    approximation = (len(in_points) / n) * (2**d)
    return approximation

def main():
    n = int(input("Random points to generate (n): "))
    d = int(input("Dimensions (d): "))
    num_processes = int(input("Number of processes: "))

    start_time = time.perf_counter()
    processes_size = n // num_processes
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        result = executor.map(volume, [(processes_size, d)] * num_processes)

    res_sum = sum(result)
    approximation = res_sum / num_processes
    exact = (math.pi**(d/2)) / math.gamma(d/2 + 1)
    end_time = time.perf_counter()

    print(f"Approximation: {approximation:.6f}")
    print(f"Exact volume: {exact:.6f}")
    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()
'''
Random points to generate (n): 10000000
Dimensions (d): 11
Number of processes: 1
Approximation: 1.915699
Exact volume: 1.884104
Time taken: 63.94 seconds

Random points to generate (n): 10000000
Dimensions (d): 11
Number of processes: 10
Approximation: 1.902182
Exact volume: 1.884104
Time taken: 28.87 seconds
'''