
N = int(input())
A = list(map(int, input().split()))

MAX = 10000

B = [0 for _ in range(N)]
C = [0 for _ in range(MAX+1)]

for i in range(N):
    C[A[i]] += 1

for i in range(1, MAX+1):
    C[i] = C[i] + C[i-1]

for i in range(N-1, -1, -1):
    C[A[i]] -= 1
    B[C[A[i]]] = A[i]

print(" ".join(map(str, B)))