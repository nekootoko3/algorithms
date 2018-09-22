N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

INFINITY = 2001
weights = [0 for _ in range(N)]
mst = [False for _ in range(N)]
mst[0] = True

while True:
    min_edge = None
    min_cost = INFINITY
    for u in range(N):
        if mst[u] == False:
            continue

        for v in range(N):
            if mst[v] == True:
                continue
            if min_cost > M[u][v] and M[u][v] != -1:
                min_cost = M[u][v]
                min_edge = v

    if min_edge is None:
        break
    mst[min_edge] = True
    weights[min_edge] = min_cost

print(sum(weights))