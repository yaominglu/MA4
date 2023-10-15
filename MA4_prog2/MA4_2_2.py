import time
from person import Person
n = 47
f = Person(n)
start_time = time.perf_counter()
fib_result_C = f.fibonacci()
end_time = time.perf_counter()
times_C = end_time - start_time
print(f"Fibonacci_C++({n}) = {fib_result_C}")
print(f"Time_C++ = {times_C:.4f} seconds")

@numba.jit(nopython=True)
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n - 1) + fib_numba(n - 2)
	
start_time_N = time.perf_counter()
result_N = fib_numba(n)
end_time_N = time.perf_counter()
times_N = end_time_N - start_time_N
print(f"Fibonacci_Numba({n}) = {result_N}")
print(f"Time_Numba = {times_N:.4f} seconds")