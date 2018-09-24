import math

N = int(input())
max_num = 0
target_list = [None for _ in range(N)]
for i in range(N):
    target = int(input())
    target_list[i] = target
    max_num = max(max_num, target)

prime_list = [True for _ in range(max_num+1)]
prime_list[0], prime_list[1] = False, False
square_root = int(math.sqrt(max_num))
for i in range(2, square_root+1):
    if prime_list[i] == False:
        continue
    j = i + i
    while j <= max_num:
        prime_list[j] = False
        j += i

cnt = 0
for i in target_list:
    if prime_list[i] == True:
        cnt += 1

print(cnt)