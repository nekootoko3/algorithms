
def dfs(src, dest, isConnected):
    for nextEdge in range(N):
        if G[src][nextEdge] == True and c[nextEdge] == WHITE:
            if dest == nextEdge:
                return True
            c[nextEdge] = GRAY
            isConnected = dfs(nextEdge, dest, isConnected)
            if isConnected:
                return isConnected
    c[src] = BLACK
    return isConnected

WHITE = 0
GRAY = 1
BLACK = 2

N, M = map(int, input().split())
G = [[False for i in range(N)] for j in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = True
    G[b][a] = True

Q = int(input())
for _ in range(Q):
    src, dest = map(int, input().split())
    c = [WHITE for _ in range(N)]
    c[src] = GRAY
    isConnected = dfs(src, dest, False)
    if isConnected:
        print("yes")
    else:
        print("no")
