import time
def solve(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True
N = int(input())
print('Yes' if solve(N) else 'No')
start = time.time()
end = time.time()
print(f'slove() elaped time: {end - start}')
    




