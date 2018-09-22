import heapq

INFTY = 1<<20

N = int(input())
M = [[] for _ in range(N)]
for i in range(N):
    u, k, *adjacents = map(int, input().split())
    for j in range(k):
        edge = adjacents[2*j]
        weight = adjacents[2*j+1]
        M[i].append((weight, edge))

mst = [False for _ in range(N)]
d = [INFTY for _ in range(N)]
d[0] = 0
pq = []
heapq.heappush(pq, (0, 0))

while len(pq) != 0:
    u = heapq.heappop(pq)
    u_edge = u[1]
    u_cost = u[0]

    mst[u_edge] = True

    if d[u_edge] < u_cost:
        continue

    for v in M[u_edge]:
        v_edge = v[1]
        v_cost = v[0]
        if mst[v_edge] == True:
            continue
        if d[u_edge]+v_cost < d[v_edge]:
            d[v_edge] = d[u_edge]+v_cost
            heapq.heappush(pq, (d[v_edge], v_edge))

for i in range(N):
    print("{} {}".format(i, d[i]))