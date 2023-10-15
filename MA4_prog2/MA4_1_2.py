import random
import math

def volume(n, d):
    points = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    points_2= [list(map(lambda x: x**2, point)) for point in points]
    sum_p = [sum(point) for point in points_2]
    in_points = [x for x in sum_p if x <= 1]
    approximation = (len(in_points) / n) * (2**d)
    exact = math.pi**(d/2) / math.gamma(d/2 + 1)
    return approximation, exact


approximation_1, exact_1 = volume(100000, 2)
print(f"Approximation: {approximation_1}")
print(f"Exact Volume: {exact_1}")

approximation_2, exact_2 = volume(100000, 11)
print(f"Approximation: {approximation_2}")
print(f"Exact Volume: {exact_2}")