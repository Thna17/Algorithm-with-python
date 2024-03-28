import time
def solve(n):    
    count = 0
    for i in range(1, n + 1):
        if N % i == 0:
            count +=1
    return count
N = int(input())
start = time.time()
print(solve(N))
end = time.time()
print(f'slove() elapsed time: {end - start}')