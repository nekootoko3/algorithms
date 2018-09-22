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
    for i in range(N):
        if mst[i] != True and d[i] < min_cost:
            min_cost = d[i]
            u = i

    if u is None:
        break

    mst[u] = True

    for v in range(N):
        if M[u][v] == INFTY:
            continue

        if d[v] == INFTY or ( d[v] > (d[u] + M[u][v]) ):
            d[v] = d[u] + M[u][v]
            p[v] = u

for i in range(N):
    print("{} {}".format(i, d[i]))