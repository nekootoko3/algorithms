from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2

N = int(input())
M = [[False for i in range(N)] for j in range(N)]
for i in range(N):
    u, k, *adjacents = map(int, input().split())
    for a in adjacents:
        M[i][a-1] = True

colors = [WHITE for _ in range(N)]
d = [-1 for _ in range(N)]

Q = deque([0], N)
colors[0] = GRAY
d[0] = 0
while len(Q) != 0:
    u = Q.popleft()
    for i in range(N):
        if M[u][i] == True and colors[i] == WHITE:
            d[i] = d[u]+1
            Q.append(i)
            colors[i] = GRAY
    colors[u] = BLACK

for i in range(N):
    print("{} {}".format(str(i+1), d[i]))