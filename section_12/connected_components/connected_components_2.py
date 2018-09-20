def dfs(src, groupNum):
    if groups[src] != 0:
        return
    groups[src] = groupNum
    c[src] = GRAY
    for nextEdge in G[src]:
        if c[nextEdge] == WHITE:
            c[nextEdge] = GRAY
            dfs(nextEdge, groupNum)
    c[src] = BLACK

WHITE = 0
GRAY = 1
BLACK = 2

N, M = map(int, input().split())
G = [[] for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

groups = [0 for _ in range(N)]
groupNum = 1
for startPoint in range(N):
    if groups[startPoint] == 0:
        c = [WHITE for _ in range(N)]
        dfs(startPoint, groupNum)
        groupNum += 1

Q = int(input())
for _ in range(Q):
    src, dest = map(int, input().split())
    if groups[src] == groups[dest]:
        print("yes")
    else:
        print("no")
