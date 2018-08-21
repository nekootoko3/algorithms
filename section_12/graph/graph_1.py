N = int(input())
adj = [[0 for j in range(N)] for i in range(N)]
for _ in range(N):
    u, k, *v = input().split()
    for i in v:
        adj[int(u)-1][int(i)-1] = 1

for a in adj:
    print(" ".join(map(str, a)))