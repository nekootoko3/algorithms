N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

match_count = 0
for i in T:
    for j in S:
        if i == j:
            match_count += 1
            break

print(str(match_count))
