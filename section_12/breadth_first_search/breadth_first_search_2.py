from collections import deque

N = int(input())
M = [[False for i in range(N)] for j in range(N)]
for edge in range(N):
    u, k, *adjacents = map(int, input().split())
    M[edge] = adjacents

Q = deque([0], N)
dist = [-1 for _ in range(N)]
dist[0] = 0
while len(Q) != 0:
    u = Q.popleft()
    for edge in M[u]:
        edge -= 1
        if dist[edge] == -1:
            dist[edge] = dist[u]+1
            Q.append(edge)

for i in range(N):
    print("{} {}".format(str(i+1), dist[i]))