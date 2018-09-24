import math

def is_prime(target):
    if target < 2:
        return False
    elif target == 2:
        return True

    if target % 2 == 0:
        return False

    i = 3
    while i*i <= target:
        if target % i == 0:
            return False
        i += 2

    return True

N = int(input())
cnt = 0
for i in range(N):
    target = int(input())
    if is_prime(target):
        cnt += 1

print(cnt)