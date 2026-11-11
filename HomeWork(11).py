
import time


n = 500000
target = 499999


numbers_list = list(range(n))
numbers_set = set(numbers_list)


start = time.perf_counter()
result_list = target in numbers_list
list_time = time.perf_counter() - start


start = time.perf_counter()
result_set = target in numbers_set
set_time = time.perf_counter() - start


print("List search:", round(list_time, 6), "сек")
print("Set search:", round(set_time, 6), "сек")

print("List:", result_list)
print("Set:", result_set)
