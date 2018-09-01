def lcs(X, Y):
    X = ' ' + X
    Y = ' ' + Y
    m = len(X)
    n = len(Y)
    c = [[None for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    max1 = 0
    for i in range(1, m):
        for j in range(1, n):
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
            max1 = max(max1, c[i][j])
    return max1


N = int(input())

for _ in range(N):
    X = input()
    Y = input()
    cnt = lcs(X, Y)
    print(cnt)