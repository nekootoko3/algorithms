N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

match_count = 0
for i in T:
    if i in S:
        match_count += 1

print(str(match_count))