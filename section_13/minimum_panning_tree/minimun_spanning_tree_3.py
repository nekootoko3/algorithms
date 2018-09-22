N = int(input())
M = []
for _ in range(N):
    M.append(list(map(int, input().split())))

INFINITY = 2001
WHITE = 0
GRAY = 1
BLACK = 2

mst = [False for _ in range(N)]
# d[u]: 頂点uへの重み
d = [INFINITY for _ in range(N)]
d[0] = 0
# p[u]: MSTにおける頂点uの親(回答には不要)
p = [-1 for _ in range(N)]
p[0] = 0
while True:
    min_cost = INFINITY
    u = None
    # MSTに加える頂点を決定する
    for i in range(N):
        # MSTではなく、既存のMSTからつながりのある頂点で辺の重みが最も小さいものを頂点uとする
        if mst[i] != True and d[i] < min_cost:
            min_cost = d[i]
            u = i
    
    if min_cost == INFINITY:
        break
    
    # 頂点uをMSTに加える
    mst[u] = True

    # 新たにMSTに加えられた頂点uから各頂点への重みを調べ、記録済みの重みより小さい場合は重みを更新する
    for v in range(N):
        if mst[v] != True and M[u][v] != -1:
            if M[u][v] < d[v]:
                d[v] = M[u][v]
                p[v] = u

print(sum(d))