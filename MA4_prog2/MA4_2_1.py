import time
import numba
import matplotlib.pyplot as plt
from person import Person
num1 = int(input('time from: '))
num2 = int(input('time to: '))
value_1 = list(range(num1, num2))
times_1 = []
for n in value_1:
	f = Person(n)
	start_time = time.perf_counter()
	f.fibonacci()
	end_time = time.perf_counter()
	times_1.append(end_time - start_time)

def fib_py(n):
	if n <= 1:
		return n
	else:
		return fib_py(n - 1) + fib_py(n - 2)
value_2 = list(range(num1, num2))
times_2 = []
for n in value_2:
	start_time = time.perf_counter()
	result = fib_py(n)
	end_time = time.perf_counter()
	time_taken = end_time - start_time
	times_2.append(time_taken)

@numba.jit(nopython=True)
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n - 1) + fib_numba(n - 2)
value_3 = list(range(num1, num2))
times_3 = []
for n in value_3:
	start_time = time.perf_counter()
	result = fib_numba(n)
	end_time = time.perf_counter()
	time_taken = end_time - start_time
	times_3.append(time_taken)

def main():
    plt.figure()
    plt.plot(value_2, times_2, marker='o',
             linestyle='-', label='Python', color='b')
    plt.plot(value_3, times_3, marker='o',
             linestyle='-', label='Numba', color='y')
    plt.plot(value_1, times_1, marker='o',
             linestyle='-', label='C++', color='r')
    plt.ylabel('Time (seconds)')
    plt.xlabel('n')
    plt.title('Calculation of the fibonacci')
    plt.legend(loc='upper right')
    plt.grid(True)
    file_name = input("Save the png file as: ")
    plt.savefig(file_name)


if __name__ == '__main__':
    main()