import sys

n = int(input())
values_string = input()

if not (2 <= n <= 10):
    sys.exit()

values_list = list(map(int, values_string.split()))
for value in values_list:
    if not (-100 <= value <= 100):
        sys.exit()

unique_values = list(set(values_list))
unique_values.sort(reverse=True)

runner_up = unique_values[1]
print(runner_up)