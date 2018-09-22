INFTY = 100001

N = int(input())
M = [[INFTY for i in range(N)] for j in range(N)]
for i in range(N):
    u, k, *adjacents = map(int, input().split())
    for j in range(k):
        edge = adjacents[j*2]
        weight = adjacents[j*2+1]
        M[u][edge] = weight

mst = [False for _ in range(N)]
d = [INFTY for _ in range(N)]
d[0] = 0
p = [-1 for _ in range(N)]
p[0] = 0
while True:
    min_cost = INFTY
    u = None
    # mstに存在せず、視点から最も近い頂点uを選択する
    for i in range(N):
        if mst[i] != True and d[i] < min_cost:
            min_cost = d[i]
            u = i

    if u is None:
        break

    mst[u] = True

    # 始点 -> 頂点u -> 頂点v への合計の重みが、これまでに記録したvへの最小の重みd[v]より小さい場合には更新する
    for v in range(N):
        # u -> への経路がない or 既に最短経路が求められている頂点の場合
        if M[u][v] == INFTY or mst[v] == True:
            continue

        # 頂点vに到達するのが初めて or 頂点u経由で頂点vに到達した方が近い
        if d[v] == INFTY or ( d[v] > (d[u] + M[u][v]) ):
            d[v] = d[u] + M[u][v]
            p[v] = u

for i in range(N):
    print("{} {}".format(i, d[i]))