N = int(input())
cnt = 0
for i in range(N):
    target = int(input())
    if target != 2 and target % 2 == 0:
        continue

    isPrime = True
    for j in range(3, int(target/2)+1, 2):
        if target % j == 0:
            isPrime = False
    if isPrime:
        cnt += 1
print(cnt)