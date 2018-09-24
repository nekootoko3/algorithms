import math

N = int(input())
cnt = 0
for i in range(N):
    target = int(input())
    if target < 2:
        continue
    elif target == 2:
        cnt += 1
        continue
    elif target % 2 == 0:
        continue

    square_root = math.sqrt(target)
    isPrime = True
    j = 3
    while j <= square_root:
        if target % j == 0:
            isPrime = False
            break
        j += 2
    if isPrime == True:
        cnt += 1

print(cnt)