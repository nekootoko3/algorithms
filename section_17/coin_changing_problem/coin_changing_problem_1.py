N, M = map(int, input().split())
C = list(map(int, input().split()))
T = [[0 for i in range(M)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(M):
        if j == 0:
            T[i][j] = i
        elif i - C[j] < 0:
            T[i][j] = T[i][j-1]
        else:
            T[i][j] = min(T[i][j-1], T[i-C[j]][j]+1)

print(T[N][M-1])