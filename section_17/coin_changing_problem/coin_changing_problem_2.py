INFTY = 50001

N, M = map(int, input().split())
C = list(map(int, input().split()))
T = [INFTY for _ in range(N+1)]
T[0] = 0

for i in range(M):
    for j in range(C[i], N+1):
        T[i] = min(T[j], T[j-C[i]]+1)

print(T[N])