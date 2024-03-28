import time
import math

def solve(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2
    if sqrt_n * sqrt_n == n:
        count -= 1
    return count

N = int(input())
start = time.time()
print(solve(N))
end = time.time()
print(f'solve() elapsed time: {end - start}')
